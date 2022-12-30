# coding=utf-8
import json
import os

import requests

from Code.Code import Sha1, Hash


class GameInstall():
    def __init__(self, GameFile_M, GameFile_V, File, Download_Source, V_JsonFile,
                 V, Name, V_Forge,V_Fabric,V_Optifine,
                 Systeam,Systeam_V,
                 Sha1Cleck):
        """
            游戏安装
            :param GameFile_M: 游戏根目录(.minecraft目录)
            :param GameFile_V: 游戏目录
            :param File: MOS缓存目录
            :param Download_Source: 下载源(MCBBS, BMCLAPI, MC)
            :param V_JsonFile: 游戏Json目录(版本列表的)
            :param V: MC版本
            :param Name: 游戏名
            :param V_Forge: Forge版本
            :param V_Fabric: Fabric版本
            :param V_Optifine: Optifine版本
            :param Systeam: 系统种类(Windows, Mac, Linux)
            :param Systeam_V: 系统版本(10,14.4.1)
            :param Sha1Cleck: 是否进行Sha1检查
        """
        self.GameFile_M = GameFile_M
        self.GameFile_V = GameFile_V
        self.File = File
        self.Download_Source = Download_Source
        self.V_JsonFile = V_JsonFile
        self.V = V
        self.Name = Name
        self.V_Forge = V_Forge
        self.V_Fabric = V_Fabric
        self.V_Optifine = V_Optifine
        self.Systeam = Systeam
        self.Systeam_V = Systeam_V
        self.Sha1Cleck = Sha1Cleck

        if self.Download_Source == 'MC':
            # self.Download_Source_Url_Json_Q = 'http://launchermeta.mojang.com/'
            self.Download_Source_Url_Libraries_Q = 'http://libraries.minecraft.net/'  # 依赖
            self.Download_Source_Url_Resources_Q = 'http://resources.download.minecraft.net/'  # 资源文件
        elif self.Download_Source == 'MCBBS':
            self.Download_Source_Url_Json_Q = 'http://download.mcbbs.net/'  # json文件
            self.Download_Source_Url_Libraries_Q = 'http://download.mcbbs.net/maven/'  # 依赖
            self.Download_Source_Url_Resources_Q = 'http://download.mcbbs.net/assets/'  # 资源文件
        else:
            self.Download_Source_Url_Json_Q = 'http://bmclapi2.bangbang93.com/'  # json文件
            self.Download_Source_Url_Libraries_Q = 'http://bmclapi2.bangbang93.com/maven/'  # 依赖
            self.Download_Source_Url_Resources_Q = 'http://bmclapi2.bangbang93.com/assets/'  # 资源文件


        super(GameInstall, self).__init__()

    def Run(self):
        # 下载MC Json文件
        # 拼接路径
        if self.Download_Source == 'MC':
            with open(self.V_JsonFile, 'r', encoding='utf_8') as f:
                b = json.load(f)
            for b_1 in b['versions']:
                if b_1['id'] == self.MC:
                    url = b_1['url']
                    break
        else:
            url = self.Download_Source_Url_Json_Q + 'version/' + self.V + '/json'

        # 下载
        V_Json_Get = requests.get(url)
        V_Json = V_Json_Get.json()
        V_Json['id'] = self.Name
        os.makedirs(self.GameFile_V, exist_ok=True)
        V_Json_File = os.path.join(self.GameFile_V,str(self.Name + '.json'))
        with open(V_Json_File, 'w+', encoding='utf-8') as f:
            json.dump(V_Json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

        # 下载Assets List Json文件
        AssetsList_Json = V_Json['assetIndex']
        try:
            url = self.Download_Source_Url_Json_Q + AssetsList_Json['url'].split('https://piston-meta.mojang.com/')[1]
        except IndexError:
            url = self.Download_Source_Url_Json_Q + AssetsList_Json['url'].split('https://launchermeta.mojang.com/')[1]
        id = AssetsList_Json['id']
        path_up = os.path.join(self.GameFile_M, 'assets', 'indexes')
        path = os.path.join(path_up, id + '.json')
        AssetsList_Json_Get = requests.get(url)
        AssetsList_Json = AssetsList_Json_Get.json()
        os.makedirs(path_up, exist_ok=True)
        with open(path, 'w+', encoding='utf-8') as f:
            json.dump(AssetsList_Json, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

        Libraries = []
        Assets = []

        import re
        # Libraries文件解析
        for L in V_Json['libraries']:
            if 'rules' in L:
                for R in L['rules']:
                    if len(R) != 1:
                        if R['action'] == 'disallow':
                            # 如果写的是禁止
                            R.pop('action')
                            for a in R:
                                if R[a]['name'] == 'osx':
                                    if self.Systeam == 'Mac':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m == None:
                                            # 如果不在限制以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up,A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-osx']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-osx']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])

                                elif R[a]['name'] == 'windows':
                                    if self.Systeam == 'Win':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m == None:
                                            # 如果不在限制以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up, A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-windows']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-windows']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                                
                                elif R[a]['name'] == 'linux':
                                    if self.Systeam == 'Linux':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m == None:
                                            # 如果不在限制以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up, A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-linux']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-linux']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])

                        elif R['action'] == 'allow':
                            # 如果写的是允许
                            R.pop('action')
                            for a in R:
                                if R[a]['name'] == 'osx':
                                    if self.Systeam == 'Mac':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m != None:
                                            # 如果在允许以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up,A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-osx']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-osx']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])

                                elif R[a]['name'] == 'windows':
                                    if self.Systeam == 'Win':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m != None:
                                            # 如果在允许以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up,A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-windows']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-windows']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])

                                elif R[a]['name'] == 'linux':
                                    if self.Systeam == 'Linux':
                                        # 如果系统匹配就进行正则表达式判断
                                        if 'version' in R[a]:
                                            # 如果写了系统版本限制规则
                                            r = R[a]['version']
                                            m = re.search(r, self.Systeam_V)
                                        else:
                                            m = ''  # 让下面的if, 识别为"允许"
                                        Sh = A['sha1']
                                        if m != None:
                                            # 如果在允许以内,就添加
                                            URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                                            Path_Up = os.path.join(self.GameFile_M, 'libraries')
                                            Path = os.path.join(Path_Up,A['path'])
                                            if os.path.exists(Path):
                                                # 如果目录存在
                                                if self.Sha1Cleck:
                                                    s = Sha1(Path)
                                                    if s != Sh:
                                                        if 'artifact' in L['downloads']:
                                                            A = L['downloads']['artifact']
                                                            Zip = False
                                                        else:
                                                            A = L['downloads']['classifiers']['natives-linux']
                                                            Zip = True
                                                        Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])
                                            else:
                                                if 'artifact' in L['downloads']:
                                                    A = L['downloads']['artifact']
                                                    Zip = False
                                                else:
                                                    A = L['downloads']['classifiers']['natives-linux']
                                                    Zip = True
                                                Libraries.append([URL, Path_Up, Path, A['size'], Sh, Zip])

            else:
                # 没有规则限制
                if self.Systeam == 'Mac':
                    if 'artifact' in L['downloads']:
                        A = L['downloads']['artifact']
                        Zip = False
                    else:
                        A = L['downloads']['classifiers']['natives-osx']
                        Zip = True
                elif self.Systeam == 'Win':
                    if 'artifact' in L['downloads']:
                        A = L['downloads']['artifact']
                        Zip = False
                    else:
                        A = L['downloads']['classifiers']['natives-windows']
                        Zip = True
                elif self.Systeam == 'Linux':
                    if 'artifact' in L['downloads']:
                        A = L['downloads']['artifact']
                        Zip = False
                    else:
                        A = L['downloads']['classifiers']['natives-linux']
                        Zip = True
                URL = self.Download_Source_Url_Libraries_Q + A['url'].split('https://libraries.minecraft.net/')[1]
                Path_Up = os.path.join(self.GameFile_M, 'libraries')
                Path = os.path.join(Path_Up, A['path'])
                Libraries.append([URL, Path_Up,Path, A['size'], A['sha1'], Zip])

        # Assets文件解析
        for A in AssetsList_Json['objects']:
            hash = AssetsList_Json['objects'][A]['hash']
            url = self.Download_Source_Url_Resources_Q + hash[0:2] + '/' +hash
            size = AssetsList_Json['objects'][A]['size']
            path_up = os.path.join(self.GameFile_M,'assets','objects',hash[0:2])
            path = os.path.join(path_up,hash)
            if os.path.exists(path):
                # 如果文件存在就判断hash值
                h = Hash(path)
                if h != hash:
                    Assets.append([url, path_up, path, hash, size])
            else:
                Assets.append([url, path_up, path, hash, size])

        print(Libraries)
        print(len(Libraries))
        print('================')
        print(Assets)
        print(len(Assets))





if __name__ == '__main__':
    #a = GameInstall('/Users/xyj/Documents/.minecraft','/Users/xyj/Documents/.minecraft/versions/1.18.1/','/Users/xyj/Documents/.MOS','MCBBS','/Users/xyj/Documents/.MOS/Versions/Versions.json',
    #      '1.18.1','1.18.1',None,None,None,'Mac','11.6.5',True)
    a = GameInstall('/Users/xyj/Documents/.minecraft', '/Users/xyj/Documents/.minecraft/versions/a1.0.11/',
                    '/Users/xyj/Documents/.MOS', 'MCBBS', '/Users/xyj/Documents/.MOS/Versions/Versions.json',
                    'a1.0.11', 'a1.0.11', None, None, None,'Mac','11.6.5',True)
    #a = GameInstall('/Users/xyj/Documents/.minecraft', '/Users/xyj/Documents/.minecraft/versions/1.9.1/',
    #                '/Users/xyj/Documents/.MOS', 'MCBBS', '/Users/xyj/Documents/.MOS/Versions/Versions.json',
    #                '1.9.1', '1.9.1', None, None, None,'Mac','11.6.5',True)
    a.Run()