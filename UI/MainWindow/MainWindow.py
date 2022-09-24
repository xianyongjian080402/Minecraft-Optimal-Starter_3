# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import UI.MainWindow.img_rc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 612)
        MainWindow.setStyleSheet("/*\n"
"    主页面qss\n"
"*/\n"
"#page_main{\n"
"    /*主页面背景*/\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#widget_Sidebar{\n"
"    /*左边栏背景*/\n"
"    border-image: url(:/Scrub/images/Scrub_B10_V.png);\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"    /*阴影 不生效 已经该用图片*/\n"
"    /*\n"
"    border-top: 5px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"    border-left: 5px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-bottom: 5px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  rgb(0, 0, 0));\n"
"    border-right: 5px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 rgb(0, 0, 0));\n"
"    */\n"
"}\n"
"#widget_Sidebar QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"#stackedWidget_main_2{\n"
"    border-image: url(:/Scrub/images/Scrub_B2_FFFFFF-50_Main-M-B.png);\n"
"}\n"
"\n"
"/*\n"
"    加载页面qss\n"
"*/\n"
"#pushButton_loading_gif{\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"#widget_page_loading{\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-image: url(:/helo_loading/images/Loading_BlackGround.gif);\n"
"}\n"
"\n"
"/*\n"
"    欢迎页面qss\n"
"*/\n"
"#stackedWidget_main #page_initialize{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(233, 233, 233, 255));\n"
"}\n"
"#page_hello{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-image: url(:/hello/images/Hello_BlackGround.png);\n"
"}\n"
"#pushButton_hello_icon{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#label_hello_text_1{\n"
"    border-image: url(:/hello/images/Hello_Text_1.png);\n"
"}\n"
"#pushButton_hello_text{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#pushButton_hello_start{\n"
"    background-color: rgb(129, 182, 243);\n"
"    color: rgb(229, 229, 229);\n"
"    border-style:none;\n"
"}\n"
"#pushButton_hello_line{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.gridLayout = QtWidgets.QGridLayout(self.page_main)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_Sidebar = QtWidgets.QWidget(self.page_main)
        self.widget_Sidebar.setEnabled(True)
        self.widget_Sidebar.setMaximumSize(QtCore.QSize(105, 16777215))
        self.widget_Sidebar.setStyleSheet("")
        self.widget_Sidebar.setObjectName("widget_Sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_Sidebar)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Sidebar_Back = QtWidgets.QPushButton(self.widget_Sidebar)
        self.pushButton_Sidebar_Back.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Back.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_Back.setIcon(icon)
        self.pushButton_Sidebar_Back.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_Back.setObjectName("pushButton_Sidebar_Back")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_Back)
        self.pushButton_Sidebar_User = QtWidgets.QPushButton(self.widget_Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Sidebar_User.sizePolicy().hasHeightForWidth())
        self.pushButton_Sidebar_User.setSizePolicy(sizePolicy)
        self.pushButton_Sidebar_User.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_User.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_User.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/User.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_User.setIcon(icon1)
        self.pushButton_Sidebar_User.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_User.setObjectName("pushButton_Sidebar_User")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_User)
        self.pushButton_Sidebar_Home = QtWidgets.QPushButton(self.widget_Sidebar)
        self.pushButton_Sidebar_Home.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Home.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Home.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_Home.setIcon(icon2)
        self.pushButton_Sidebar_Home.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_Home.setObjectName("pushButton_Sidebar_Home")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_Home)
        self.pushButton_Sidebar_OnLine = QtWidgets.QPushButton(self.widget_Sidebar)
        self.pushButton_Sidebar_OnLine.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_OnLine.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_OnLine.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Online.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_OnLine.setIcon(icon3)
        self.pushButton_Sidebar_OnLine.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_OnLine.setObjectName("pushButton_Sidebar_OnLine")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_OnLine)
        self.pushButton_Sidebar_Download = QtWidgets.QPushButton(self.widget_Sidebar)
        self.pushButton_Sidebar_Download.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Download.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Download.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_Download.setIcon(icon4)
        self.pushButton_Sidebar_Download.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_Download.setObjectName("pushButton_Sidebar_Download")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_Download)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_Sidebar_Settings = QtWidgets.QPushButton(self.widget_Sidebar)
        self.pushButton_Sidebar_Settings.setMinimumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Settings.setMaximumSize(QtCore.QSize(49, 47))
        self.pushButton_Sidebar_Settings.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Sidebar_Settings.setIcon(icon5)
        self.pushButton_Sidebar_Settings.setIconSize(QtCore.QSize(47, 47))
        self.pushButton_Sidebar_Settings.setObjectName("pushButton_Sidebar_Settings")
        self.verticalLayout.addWidget(self.pushButton_Sidebar_Settings)
        self.gridLayout.addWidget(self.widget_Sidebar, 0, 0, 1, 1)
        self.widget_Middle = QtWidgets.QWidget(self.page_main)
        self.widget_Middle.setObjectName("widget_Middle")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_Middle)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget_main_2 = QtWidgets.QStackedWidget(self.widget_Middle)
        self.stackedWidget_main_2.setObjectName("stackedWidget_main_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_main_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_main_2.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget_main_2)
        self.gridLayout.addWidget(self.widget_Middle, 0, 1, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main)
        self.page_initialize = QtWidgets.QWidget()
        self.page_initialize.setObjectName("page_initialize")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_initialize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 3, 1, 1)
        self.widget_page_loading = QtWidgets.QWidget(self.page_initialize)
        self.widget_page_loading.setMinimumSize(QtCore.QSize(161, 172))
        self.widget_page_loading.setObjectName("widget_page_loading")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_page_loading)
        self.gridLayout_4.setContentsMargins(22, 22, 22, 22)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_loading_text_2 = QtWidgets.QLabel(self.widget_page_loading)
        self.label_loading_text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading_text_2.setObjectName("label_loading_text_2")
        self.gridLayout_4.addWidget(self.label_loading_text_2, 4, 0, 1, 1)
        self.pushButton_loading_gif = QtWidgets.QPushButton(self.widget_page_loading)
        self.pushButton_loading_gif.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/MOS_Logo_gif.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_loading_gif.setIcon(icon6)
        self.pushButton_loading_gif.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_loading_gif.setObjectName("pushButton_loading_gif")
        self.gridLayout_4.addWidget(self.pushButton_loading_gif, 1, 0, 1, 1)
        self.label_loading_text_1 = QtWidgets.QLabel(self.widget_page_loading)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_loading_text_1.setFont(font)
        self.label_loading_text_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading_text_1.setObjectName("label_loading_text_1")
        self.gridLayout_4.addWidget(self.label_loading_text_1, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget_page_loading)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_page_loading, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 2, 2, 1, 1)
        self.stackedWidget_main.addWidget(self.page_initialize)
        self.page_hello = QtWidgets.QWidget()
        self.page_hello.setObjectName("page_hello")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_hello)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 2, 3, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 0, 3, 1)
        self.widget_hello = QtWidgets.QWidget(self.page_hello)
        self.widget_hello.setObjectName("widget_hello")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_hello)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 3, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 0, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 3, 2, 1, 1)
        self.pushButton_hello_text = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_text.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Text.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_text.setIcon(icon7)
        self.pushButton_hello_text.setIconSize(QtCore.QSize(327, 153))
        self.pushButton_hello_text.setObjectName("pushButton_hello_text")
        self.gridLayout_6.addWidget(self.pushButton_hello_text, 1, 2, 2, 3)
        self.pushButton_hello_start = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_start.setMinimumSize(QtCore.QSize(173, 43))
        self.pushButton_hello_start.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Text_Start.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_start.setIcon(icon8)
        self.pushButton_hello_start.setIconSize(QtCore.QSize(173, 43))
        self.pushButton_hello_start.setObjectName("pushButton_hello_start")
        self.gridLayout_6.addWidget(self.pushButton_hello_start, 3, 3, 2, 1)
        self.pushButton_hello_icon = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_icon.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_icon.setIcon(icon9)
        self.pushButton_hello_icon.setIconSize(QtCore.QSize(253, 253))
        self.pushButton_hello_icon.setObjectName("pushButton_hello_icon")
        self.gridLayout_6.addWidget(self.pushButton_hello_icon, 0, 0, 6, 1)
        self.pushButton_hello_line = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_line.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Line_Vertical.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_line.setIcon(icon10)
        self.pushButton_hello_line.setIconSize(QtCore.QSize(21, 253))
        self.pushButton_hello_line.setObjectName("pushButton_hello_line")
        self.gridLayout_6.addWidget(self.pushButton_hello_line, 0, 1, 6, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem12, 5, 2, 1, 3)
        self.gridLayout_5.addWidget(self.widget_hello, 1, 1, 1, 1)
        self.stackedWidget_main.addWidget(self.page_hello)
        self.horizontalLayout_2.addWidget(self.stackedWidget_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOS Ⅲ 启动器"))
        self.label_loading_text_2.setText(_translate("MainWindow", "正在读取设置(1/2)"))
        self.label_loading_text_1.setText(_translate("MainWindow", "正在初始化启动器……"))
