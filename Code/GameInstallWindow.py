# coding=utf-8
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QPropertyAnimation, Qt, pyqtSignal, QThread, QTimer
from PyQt6.QtGui import QColor

from UI.GameInstallWindow.GameInstallWindow import Ui_Dialog_GameInstall
from Code.MainWindow import Return_Window_XY
from PyQt6.QtWidgets import QDialog, QGraphicsDropShadowEffect

import UI.Dialog_All_rc

class Dialog_GameInstallWindows_(QDialog, Ui_Dialog_GameInstall):
    sinOut_Win_XY = pyqtSignal(int, int)
    sinOut_OK = pyqtSignal()

    def __init__(self, GameFile_M, GameFile_V, File, Download_Source, V_JsonFile,
                 V, Name, V_Forge,V_Fabric,V_Optifine,
                 Systeam,Systeam_V,
                 AssetsFileDownloadMethod,Sha1Cleck,MaxConcurrence):
        """
            游戏安装窗口
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
            :param AssetsFileDownloadMethod: 资源文件下载方式(A,B-尚未完成)
            :param Sha1Cleck: 是否进行Sha1检查
            :param MaxConcurrence: 最大并发数
        """

        super(Dialog_GameInstallWindows_, self).__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_bottom_cancel.clicked.connect(self.stop)
        #self.pushButton_OffLine_Advanced.clicked.connect(self.pushButton_OffLine_Advanced_Clicked)
        #self.pushButton_bottom_cancel_confirm.clicked.connect(self.pushButton_Confirm_Clicked)

        self.OffLine_Advanced_Open = False  # 存储现在 离线登陆中的"高级选项"是否打开

        # 添加阴影
        self.effect_shadow = QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(2, 3)  # 偏移 (向右,向下)
        self.effect_shadow.setColor(QColor(121, 121, 121, 200))  # 阴影颜色
        self.effect_shadow.setBlurRadius(18)  # 阴影圆角
        self.setGraphicsEffect(self.effect_shadow)  # 将设置套用到窗口中

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
        self.AssetsFileDownloadMethod = AssetsFileDownloadMethod
        self.Sha1Cleck = Sha1Cleck
        self.MaxConcurrence = MaxConcurrence

    def Run(self):
        self.Install_Thread_ = \
            Install_Thread(self.GameFile_M, self.GameFile_V, self.File, self.Download_Source, self.V_JsonFile,
                           self.V, self.Name, self.V_Forge,self.V_Fabric,self.V_Optifine,
                           self.Systeam,self.Systeam_V,
                           self.AssetsFileDownloadMethod,self.Sha1Cleck,self.MaxConcurrence)
        self.Install_Thread_.SinOut.connect(self.SinOut)
        self.Install_Thread_.start()

    def SinOut(self,text):
        print(text)
        if text[0] == 'start':
            # 如果进度是初始化
            self.progressBar_start.setMaximum(text[2])
            self.progressBar_start.setValue(text[1])

        elif text[0] == 'info':
            # 如果是报告下载量的
            if text[1] == 0:
                self.librarysFileNoNone = False
                self.progressBar_inatall_libraryFile.setMaximum(-1)
                self.progressBar_inatall_libraryFile.setMinimum(-2)
                self.progressBar_inatall_libraryFile.setValue(-1)
            else:
                self.librarysFileNoNone = True
                self.progressBar_inatall_libraryFile.setMaximum(text[1])
            if text[2] == 0:
                self.assetsFileNoNone = False
                self.progressBar_inatall_assetsFile.setMaximum(-1)
                self.progressBar_inatall_assetsFile.setMinimum(-2)
                self.progressBar_inatall_assetsFile.setValue(-1)
            else:
                self.assetsFileNoNone = True
                self.progressBar_inatall_assetsFile.setMaximum(text[2])

            t = round(text[3]/1024/1024,2)  # 四舍五入保留2位
            self.label_info_size.setText('0MB/'+str(t)+'MB')
            self.stackedWidget.setCurrentIndex(1)

        elif text[0] == 'download':
            # 如果是正在下载
            if self.librarysFileNoNone:
                self.progressBar_inatall_libraryFile.setValue(text[1])

            if self.assetsFileNoNone:
                self.progressBar_inatall_assetsFile.setValue(text[2])

            t = round(text[3]/1024/1024,2)  # 四舍五入保留2位
            self.label_info_size.setText(
                str(t) + 'MB/' + str(self.label_info_size.text()).split('/')[1]
            )
            self.label_Sidebar_B_QTime = QTimer()
            self.label_Sidebar_B_QTime.start(1000)
            self.label_Sidebar_B_QTime.timeout.connect(self.Spend_QTime)

        elif text[0] == 'JarProgress':
            # 如果在进行Jar下载
            a = text[1]
            if a[0] == 'start':
                # 如果进入初始化
                self.progressBar_inatall_Jar.setMaximum(a[1])
            elif a[0] == 'download':
                # 如果开始下载
                self.progressBar_inatall_Jar.setValue(a[1])


        elif text[0] == 'ok':
            # 完成
            self.sinOut_OK.emit()
            self.close_()

    def Spend_QTime(self):
        try:
            print(self.Spend_)
            print(round(float(str(self.label_info_size.text()).split('MB/')[0])),2)
            a = round(float(str(self.label_info_size.text()).split('MB/')[0]) - self.Spend_,2)
            self.label_info_spend.setText(str(a) + 'MB/s')
            self.Spend_ = float(str(self.label_info_size.text()).split('MB/')[0])
        except AttributeError:
            self.Spend_ = float(str(self.label_info_size.text()).split('MB')[0])
            self.label_info_spend.setText(str(self.Spend_)+'MB/s')

    def stop(self):
        self.close_()

    def close_(self):
        def close__():
            self.close()
        try:
            self.label_Sidebar_B_QTime.stop()
        except AttributeError:
            pass
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
        self.anim.setDuration(300)  # 设置动画时长
        self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
        self.anim.finished.connect(close__)  # 动画结束时，关闭窗口
        self.anim.start()  # 开始动画


    def clicked_pushButton_close(self):
        self.pushButton_bottom_cancel.setEnabled(False)  # 为了防止重复操作 直接禁用按钮
        self.anim = QPropertyAnimation(self, b"windowOpacity")  # 设置动画对象
        self.anim.setDuration(300)  # 设置动画时长
        self.anim.setStartValue(1)  # 设置初始属性，1.0为不透明
        self.anim.setEndValue(0)  # 设置结束属性，0为完全透明
        self.anim.finished.connect(self.close_)  # 动画结束时，关闭窗口
        self.anim.start()  # 开始动画

    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        self.Is_Drag_ = True
        self.Mouse_Start_Point_ = a0.globalPosition()  # 获得鼠标的初始位置
        self.Window_Start_Point_ = self.frameGeometry().topLeft()  # 获得窗口的初始位置

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        # 判断是否在拖拽移动
        if self.Is_Drag_:
            # 获得鼠标移动的距离
            self.Move_Distance = a0.globalPosition() - self.Mouse_Start_Point_
            # 改变窗口的位置
            Main_XY = Return_Window_XY()
            self.sinOut_Win_XY.emit(
                round(Main_XY.x() + self.Move_Distance.x()),
                round(Main_XY.y() + self.Move_Distance.y())
            )
            x_c_m = self.Move_Distance.x()
            y_c_m = self.Move_Distance.y()
            x = self.Window_Start_Point_.x() + x_c_m
            y = self.Window_Start_Point_.y() + y_c_m
            self.move(round(x), round(y))

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        # 放下左键即停止移动
        if a0.button() == Qt.MouseButton.LeftButton:
            self.Is_Drag_ = False


class Install_Thread(QThread):
    SinOut = pyqtSignal(list)
    def __init__(self, GameFile_M, GameFile_V, File, Download_Source, V_JsonFile,
                 V, Name, V_Forge,V_Fabric,V_Optifine,
                 Systeam,Systeam_V,
                 AssetsFileDownloadMethod,Sha1Cleck,MaxConcurrence):
        """
            多线程安装
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
            :param AssetsFileDownloadMethod: 资源文件下载方式(A,B-尚未完成)
            :param Sha1Cleck: 是否进行Sha1检查
            :param MaxConcurrence: 最大并发数
        """
        super(Install_Thread, self).__init__()
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
        self.AssetsFileDownloadMethod = AssetsFileDownloadMethod
        self.Sha1Cleck = Sha1Cleck
        self.MaxConcurrence = MaxConcurrence

    def run(self):
        import gc
        from Code.MC_Code.GameInstall import GameInstall
        a = GameInstall(self.GameFile_M, self.GameFile_V, self.File, self.Download_Source, self.V_JsonFile,
                        self.V, self.Name, self.V_Forge, self.V_Fabric, self.V_Optifine,
                        self.Systeam, self.Systeam_V,
                        self.AssetsFileDownloadMethod, self.Sha1Cleck, self.MaxConcurrence, self.ProgressSinOut)
        a.Run()
        gc.collect()

    def ProgressSinOut(self,text):
        self.SinOut.emit(text)