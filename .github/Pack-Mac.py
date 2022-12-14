# python自带的库无需输入，第三方库和自己引入的自写模块需要输入
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

# 放置要执行py的列表
APP = ['main.py']

# 存放所有要用到的文件资源
DATA_FILES = ['UI','Code']

# 可选参数。
# iconfile：app的图标，必须为icns的格式，其他格式的话是不会显示出来的
# includes: A list of Python modules to include even if they are not detected by dependency checker. Packages in this list are ignored.
# includes: 第三方库放在这里。
# plist：其他的app应用配置，熟悉MACOS应用开发的都会非常熟悉这些参数，mac应用info.plist里的参数都可以添加进去
OPTIONS = {
           'plist': {
                    'CFBundleName'   : 'MOS',     # 应用名
                    'CFBundleDisplayName': 'verify', # 应用显示名
                    'CFBundleVersion': '1.0.0',      # 应用版本号
                    'CFBundleIdentifier' : 'verify', # 应用包名、唯一标识
                    'NSHumanReadableCopyright': 'Copyright © 2021 SW Felix.Zhao. All rights reserved.', # 可读版权
           'includes': ['PyQt6','urllib3']
                       }
           }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
