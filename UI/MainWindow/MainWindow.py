# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


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
"\n"
"/*取消中间页面的边框*/\n"
"#stackedWidget_main_2 > QWidget\n"
"{\n"
"    border-style:none;\n"
"}\n"
"#scrollArea_page_settings{border-style:none;}\n"
"#widget_Middle{border-style:none;}\n"
"#widget_Sidebar{\n"
"    /*左边栏背景*/\n"
"    border-image: url(:/Scrub/images/Scrub_B10_V.png);\n"
"    background: rgba(255, 255, 255, 0.5);\n"
"    /*阴影 不生效 已经使用图片*/\n"
"    /*\n"
"    border-top: 5px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"    border-left: 5px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-bottom: 5px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  rgb(0, 0, 0));\n"
"    border-right: 5px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 rgb(0, 0, 0));\n"
"    */\n"
"}\n"
"\n"
"/*左边边栏按钮设置*/\n"
"\n"
"#widget_Sidebar QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*设置页面*/\n"
"#scrollAreaWidgetContents_page_settings > QWidget\n"
"{\n"
"    border-image: url(:/widget_Sidebar/images/Scrub_Settings-Z_B15.png);\n"
"}\n"
"\n"
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
"}\n"
"\n"
"\n"
"/*单独控件qss*/\n"
"/*选择控件*/\n"
"QRadioButton {\n"
"    spacing: 10px;\n"
"    color: black;\n"
"    background-color:  rgba(255, 255, 255,0);\n"
"}\n"
"QRadioButton::indicator {\n"
"    background-color: rgba(255, 255, 255,0);\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    border: 2px solid rgb(154, 154, 154);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 8px;\n"
"    width: 8px;\n"
"    border: 7px solid rgb(42, 130, 228);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    border: 2px solid rgb(120, 120, 120);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"    height: 8px;\n"
"    width: 8px;\n"
"    border: 7px solid rgb(47, 144, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    background-color: rgb(153, 153, 153);\n"
"    border: 2px solid rgb(84, 84, 84);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:checked:pressed {\n"
"    height: 8px;\n"
"    width: 8px;\n"
"    border: 7px solid rgb(83, 163, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*QSlider*/\n"
"QSlider::groove:horizontal {\n"
"    /*滑条*/\n"
"    border: 1px solid #bbb;\n"
"    background: white;\n"
"    height: 3px;\n"
"    border-radius: 1px;\n"
"}\n"
"  \n"
"QSlider::sub-page:horizontal {\n"
"    /*已经划过的*/\n"
"    background: rgb(0, 150, 255);\n"
"    border: 1px solid rgba(255, 255, 255, 0);\n"
"    height: 3px;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    /*没有划过的*/\n"
"    background: rgb(235, 235, 235);  \n"
"    border: 1px solid rgba(255, 255, 255, 0);\n"
"    height: 3px;\n"
"    border-radius: 1px;\n"
"}\n"
" \n"
"QSlider::handle:horizontal {\n"
"    /* 上下边距和左右边距(中间的“提手”)*/\n"
"    background: rgb(0, 150, 255);\n"
"    border: 5px solid rgb(0, 150, 255);\n"
"    width: 8px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: rgb(0, 150, 255);\n"
"    border: 5px solid rgb(0, 150, 255);\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"\n"
"/*QSpinBox*/\n"
"QSpinBox {\n"
"    /* 为箭头保留空间 */\n"
"    padding-right:25px;\n"
"    border:2px solid rgb(33, 33, 33);\n"
"    background: rgba(255, 255, 255, 128);\n"
"    min-width:40px;\n"
"    border-radius: 5px;\n"
"    padding: -1;  /*改变焦点框*/\n"
"}\n"
"\n"
"QSpinBox:focus{\n"
"    /*出现光标后*/\n"
"    border:2px solid rgb(4, 51, 255);\n"
"}\n"
"\n"
"\n"
"/* 向上按钮 */\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:top right;\n"
"    width:18px;\n"
"    border-image:url(:/widget_Sidebar/images/Up.png);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.985075, y2:0, stop:0 rgba(235, 235, 235, 255), stop:1 rgba(255, 255, 255, 0));\n"
"    border-top-right-radius:5px;\n"
"    border-width:1px;\n"
"}\n"
" \n"
"/* 向上按钮 */\n"
"QSpinBox::up-button:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(225, 225, 225, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
" \n"
"/* 向上按钮 */\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(190, 190, 190, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
" \n"
"/* 向上按钮里的小箭头 */\n"
"QSpinBox::up-arrow {\n"
"    image:url(:/images/333.bmp);\n"
"    width:7px;\n"
"    height:7px;\n"
"}\n"
" \n"
"/* 向下按钮 */\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:bottom right;\n"
"    width:18px;\n"
"    border-image:url(:/widget_Sidebar/images/Dowe.png);\n"
"    border-bottom-right-radius:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(235, 235, 235, 255), stop:1 rgba(255, 255, 255, 0));\n"
"    border-width:1px;\n"
"    border-top-width:0;\n"
"}\n"
" \n"
"/* 向下按钮 */\n"
"QSpinBox::down-button:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(225, 225, 225, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
" \n"
"/* 向下按钮 */\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 190, 190, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
" \n"
"/* 向下按钮里的小箭头 */\n"
"QSpinBox::down-arrow {\n"
"    image:url(:/images/333.bmp);\n"
"    width:7px;\n"
"    height:7px;\n"
"}\n"
"\n"
"*{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"*{outline:0px;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_main.setStyleSheet("")
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setStyleSheet("/*模拟阴影*/\n"
"#widget_Middle > #stackedWidget_main_2{border-image: url(:/Scrub/images/Scrub_B2_FFFFFF-50_Main-M-B.png);}")
        self.page_main.setObjectName("page_main")
        self.gridLayout = QtWidgets.QGridLayout(self.page_main)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_Sidebar = QtWidgets.QWidget(self.page_main)
        self.widget_Sidebar.setEnabled(True)
        self.widget_Sidebar.setMaximumSize(QtCore.QSize(105, 16777215))
        self.widget_Sidebar.setStyleSheet("/*这个地方是点击按钮之后自动刷新(修改)的*/\n"
"#pushButton_Sidebar_Home{\n"
"    border-image: url(:/widget_Sidebar/images/Home-B-Black.png);\n"
"}")
        self.widget_Sidebar.setObjectName("widget_Sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_Sidebar)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Sidebar_Back = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_Back.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Back.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Back.setText("")
        self.label_Sidebar_Back.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Back.png"))
        self.label_Sidebar_Back.setScaledContents(True)
        self.label_Sidebar_Back.setObjectName("label_Sidebar_Back")
        self.verticalLayout.addWidget(self.label_Sidebar_Back)
        self.label_Sidebar_User = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_User.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_User.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_User.setText("")
        self.label_Sidebar_User.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/User.png"))
        self.label_Sidebar_User.setScaledContents(True)
        self.label_Sidebar_User.setObjectName("label_Sidebar_User")
        self.verticalLayout.addWidget(self.label_Sidebar_User)
        self.label_Sidebar_Home = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_Home.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Home.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Home.setText("")
        self.label_Sidebar_Home.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Home.png"))
        self.label_Sidebar_Home.setScaledContents(True)
        self.label_Sidebar_Home.setObjectName("label_Sidebar_Home")
        self.verticalLayout.addWidget(self.label_Sidebar_Home)
        self.label_Sidebar_OnLine = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_OnLine.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_OnLine.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_OnLine.setText("")
        self.label_Sidebar_OnLine.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Online.png"))
        self.label_Sidebar_OnLine.setScaledContents(True)
        self.label_Sidebar_OnLine.setObjectName("label_Sidebar_OnLine")
        self.verticalLayout.addWidget(self.label_Sidebar_OnLine)
        self.label_Sidebar_Download = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_Download.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Download.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Download.setText("")
        self.label_Sidebar_Download.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Download.png"))
        self.label_Sidebar_Download.setScaledContents(True)
        self.label_Sidebar_Download.setObjectName("label_Sidebar_Download")
        self.verticalLayout.addWidget(self.label_Sidebar_Download)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_Sidebar_Settings = MyQLabel(self.widget_Sidebar)
        self.label_Sidebar_Settings.setMinimumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Settings.setMaximumSize(QtCore.QSize(49, 47))
        self.label_Sidebar_Settings.setText("")
        self.label_Sidebar_Settings.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/Settings.png"))
        self.label_Sidebar_Settings.setScaledContents(True)
        self.label_Sidebar_Settings.setObjectName("label_Sidebar_Settings")
        self.verticalLayout.addWidget(self.label_Sidebar_Settings)
        self.gridLayout.addWidget(self.widget_Sidebar, 0, 0, 1, 1)
        self.widget_Middle = QtWidgets.QWidget(self.page_main)
        self.widget_Middle.setObjectName("widget_Middle")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_Middle)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget_main_2 = QtWidgets.QStackedWidget(self.widget_Middle)
        self.stackedWidget_main_2.setStyleSheet("")
        self.stackedWidget_main_2.setObjectName("stackedWidget_main_2")
        self.page_users = QtWidgets.QWidget()
        self.page_users.setObjectName("page_users")
        self.stackedWidget_main_2.addWidget(self.page_users)
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.stackedWidget_main_2.addWidget(self.page_home)
        self.page_online = QtWidgets.QWidget()
        self.page_online.setObjectName("page_online")
        self.stackedWidget_main_2.addWidget(self.page_online)
        self.page_download = QtWidgets.QWidget()
        self.page_download.setObjectName("page_download")
        self.stackedWidget_main_2.addWidget(self.page_download)
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setStyleSheet("")
        self.page_settings.setObjectName("page_settings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_settings)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_page_settings = QtWidgets.QScrollArea(self.page_settings)
        self.scrollArea_page_settings.setWidgetResizable(True)
        self.scrollArea_page_settings.setObjectName("scrollArea_page_settings")
        self.scrollAreaWidgetContents_page_settings = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_page_settings.setGeometry(QtCore.QRect(0, 0, 1119, 612))
        self.scrollAreaWidgetContents_page_settings.setObjectName("scrollAreaWidgetContents_page_settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_page_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_page_settings_h1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_page_settings)
        self.label_page_settings_h1.setScaledContents(False)
        self.label_page_settings_h1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_page_settings_h1.setObjectName("label_page_settings_h1")
        self.verticalLayout_2.addWidget(self.label_page_settings_h1)
        self.widget_page_settings_subject = QtWidgets.QWidget(self.scrollAreaWidgetContents_page_settings)
        self.widget_page_settings_subject.setObjectName("widget_page_settings_subject")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_page_settings_subject)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_page_settings_subject_h2 = QtWidgets.QLabel(self.widget_page_settings_subject)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_page_settings_subject_h2.setFont(font)
        self.label_page_settings_subject_h2.setObjectName("label_page_settings_subject_h2")
        self.horizontalLayout_3.addWidget(self.label_page_settings_subject_h2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.radioButton_settings_subject_light = QtWidgets.QRadioButton(self.widget_page_settings_subject)
        self.radioButton_settings_subject_light.setObjectName("radioButton_settings_subject_light")
        self.horizontalLayout_3.addWidget(self.radioButton_settings_subject_light)
        self.radioButton_settings_subject_dark = QtWidgets.QRadioButton(self.widget_page_settings_subject)
        self.radioButton_settings_subject_dark.setObjectName("radioButton_settings_subject_dark")
        self.horizontalLayout_3.addWidget(self.radioButton_settings_subject_dark)
        self.radioButton_settings_subject_automatic = QtWidgets.QRadioButton(self.widget_page_settings_subject)
        self.radioButton_settings_subject_automatic.setObjectName("radioButton_settings_subject_automatic")
        self.horizontalLayout_3.addWidget(self.radioButton_settings_subject_automatic)
        self.verticalLayout_2.addWidget(self.widget_page_settings_subject)
        self.widget_page_settings_background = QtWidgets.QWidget(self.scrollAreaWidgetContents_page_settings)
        self.widget_page_settings_background.setObjectName("widget_page_settings_background")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_page_settings_background)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_settings_background_none = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_none.setEnabled(True)
        self.radioButton_settings_background_none.setObjectName("radioButton_settings_background_none")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_none, 1, 0, 1, 1)
        self.radioButton_settings_background_1 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_1.setObjectName("radioButton_settings_background_1")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_1, 1, 1, 1, 1)
        self.radioButton_settings_background_2 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_2.setObjectName("radioButton_settings_background_2")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_2, 1, 2, 1, 1)
        self.radioButton_settings_background_3 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_3.setObjectName("radioButton_settings_background_3")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_3, 1, 3, 1, 1)
        self.radioButton_settings_background_4 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_4.setObjectName("radioButton_settings_background_4")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_4, 3, 0, 1, 1)
        self.radioButton_settings_background_5 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_5.setObjectName("radioButton_settings_background_5")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_5, 3, 1, 1, 1)
        self.radioButton_settings_background_6 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_6.setObjectName("radioButton_settings_background_6")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_6, 3, 2, 1, 1)
        self.radioButton_settings_background_7 = QtWidgets.QRadioButton(self.widget_page_settings_background)
        self.radioButton_settings_background_7.setObjectName("radioButton_settings_background_7")
        self.gridLayout_2.addWidget(self.radioButton_settings_background_7, 3, 3, 1, 1)
        self.label_page_settings_background_h2 = QtWidgets.QLabel(self.widget_page_settings_background)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_page_settings_background_h2.setFont(font)
        self.label_page_settings_background_h2.setObjectName("label_page_settings_background_h2")
        self.gridLayout_2.addWidget(self.label_page_settings_background_h2, 0, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.widget_page_settings_background)
        self.widget_page_settings_Sidebar = QtWidgets.QWidget(self.scrollAreaWidgetContents_page_settings)
        self.widget_page_settings_Sidebar.setStyleSheet("")
        self.widget_page_settings_Sidebar.setObjectName("widget_page_settings_Sidebar")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_page_settings_Sidebar)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_page_settings_background_h3 = QtWidgets.QLabel(self.widget_page_settings_Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_page_settings_background_h3.sizePolicy().hasHeightForWidth())
        self.label_page_settings_background_h3.setSizePolicy(sizePolicy)
        self.label_page_settings_background_h3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_page_settings_background_h3.setObjectName("label_page_settings_background_h3")
        self.gridLayout_7.addWidget(self.label_page_settings_background_h3, 1, 0, 1, 2)
        self.label_page_settings_sidebar_h2 = QtWidgets.QLabel(self.widget_page_settings_Sidebar)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_page_settings_sidebar_h2.setFont(font)
        self.label_page_settings_sidebar_h2.setObjectName("label_page_settings_sidebar_h2")
        self.gridLayout_7.addWidget(self.label_page_settings_sidebar_h2, 0, 0, 1, 2)
        self.horizontalSlider_page_settings_sidebar = QtWidgets.QSlider(self.widget_page_settings_Sidebar)
        self.horizontalSlider_page_settings_sidebar.setMaximum(70)
        self.horizontalSlider_page_settings_sidebar.setProperty("value", 15)
        self.horizontalSlider_page_settings_sidebar.setSliderPosition(15)
        self.horizontalSlider_page_settings_sidebar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_page_settings_sidebar.setObjectName("horizontalSlider_page_settings_sidebar")
        self.gridLayout_7.addWidget(self.horizontalSlider_page_settings_sidebar, 2, 0, 1, 2)
        self.spinBox_page_settings_sidebar = QtWidgets.QSpinBox(self.widget_page_settings_Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_page_settings_sidebar.sizePolicy().hasHeightForWidth())
        self.spinBox_page_settings_sidebar.setSizePolicy(sizePolicy)
        self.spinBox_page_settings_sidebar.setMinimumSize(QtCore.QSize(42, 30))
        self.spinBox_page_settings_sidebar.setMouseTracking(False)
        self.spinBox_page_settings_sidebar.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.spinBox_page_settings_sidebar.setStyleSheet("")
        self.spinBox_page_settings_sidebar.setMinimum(1)
        self.spinBox_page_settings_sidebar.setMaximum(70)
        self.spinBox_page_settings_sidebar.setProperty("value", 15)
        self.spinBox_page_settings_sidebar.setObjectName("spinBox_page_settings_sidebar")
        self.gridLayout_7.addWidget(self.spinBox_page_settings_sidebar, 2, 2, 1, 1)
        self.label_page_settings_background_h3_2 = QtWidgets.QLabel(self.widget_page_settings_Sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_page_settings_background_h3_2.sizePolicy().hasHeightForWidth())
        self.label_page_settings_background_h3_2.setSizePolicy(sizePolicy)
        self.label_page_settings_background_h3_2.setMinimumSize(QtCore.QSize(165, 16))
        self.label_page_settings_background_h3_2.setMaximumSize(QtCore.QSize(165, 16))
        self.label_page_settings_background_h3_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_page_settings_background_h3_2.setObjectName("label_page_settings_background_h3_2")
        self.gridLayout_7.addWidget(self.label_page_settings_background_h3_2, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_page_settings_Sidebar)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.scrollArea_page_settings.setWidget(self.scrollAreaWidgetContents_page_settings)
        self.verticalLayout_3.addWidget(self.scrollArea_page_settings)
        self.stackedWidget_main_2.addWidget(self.page_settings)
        self.horizontalLayout.addWidget(self.stackedWidget_main_2)
        self.gridLayout.addWidget(self.widget_Middle, 0, 1, 1, 1)
        self.stackedWidget_main.addWidget(self.page_main)
        self.page_initialize = QtWidgets.QWidget()
        self.page_initialize.setObjectName("page_initialize")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_initialize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 3, 1, 1)
        self.widget_page_loading = QtWidgets.QWidget(self.page_initialize)
        self.widget_page_loading.setMinimumSize(QtCore.QSize(161, 172))
        self.widget_page_loading.setObjectName("widget_page_loading")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_page_loading)
        self.gridLayout_4.setContentsMargins(22, 22, 22, 22)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_loading_gif = QtWidgets.QLabel(self.widget_page_loading)
        self.label_loading_gif.setMaximumSize(QtCore.QSize(80, 80))
        self.label_loading_gif.setText("")
        self.label_loading_gif.setPixmap(QtGui.QPixmap(":/widget_Sidebar/images/MOS_Logo_gif.gif"))
        self.label_loading_gif.setScaledContents(True)
        self.label_loading_gif.setObjectName("label_loading_gif")
        self.gridLayout_4.addWidget(self.label_loading_gif, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 1, 2, 1, 1)
        self.label_loading_text_1 = QtWidgets.QLabel(self.widget_page_loading)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_loading_text_1.setFont(font)
        self.label_loading_text_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading_text_1.setObjectName("label_loading_text_1")
        self.gridLayout_4.addWidget(self.label_loading_text_1, 2, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.widget_page_loading)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 0, 1, 3)
        self.label_loading_text_2 = QtWidgets.QLabel(self.widget_page_loading)
        self.label_loading_text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading_text_2.setObjectName("label_loading_text_2")
        self.gridLayout_4.addWidget(self.label_loading_text_2, 4, 0, 1, 3)
        self.gridLayout_3.addWidget(self.widget_page_loading, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 2, 2, 1, 1)
        self.stackedWidget_main.addWidget(self.page_initialize)
        self.page_hello = QtWidgets.QWidget()
        self.page_hello.setObjectName("page_hello")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_hello)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 0, 2, 3, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem11, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 0, 0, 3, 1)
        self.widget_hello = QtWidgets.QWidget(self.page_hello)
        self.widget_hello.setObjectName("widget_hello")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_hello)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 3, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem14, 0, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem15, 3, 2, 1, 1)
        self.pushButton_hello_text = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_text.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Text.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_text.setIcon(icon)
        self.pushButton_hello_text.setIconSize(QtCore.QSize(327, 153))
        self.pushButton_hello_text.setObjectName("pushButton_hello_text")
        self.gridLayout_6.addWidget(self.pushButton_hello_text, 1, 2, 2, 3)
        self.pushButton_hello_start = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_start.setMinimumSize(QtCore.QSize(173, 43))
        self.pushButton_hello_start.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Text_Start.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_start.setIcon(icon1)
        self.pushButton_hello_start.setIconSize(QtCore.QSize(173, 43))
        self.pushButton_hello_start.setObjectName("pushButton_hello_start")
        self.gridLayout_6.addWidget(self.pushButton_hello_start, 3, 3, 2, 1)
        self.pushButton_hello_icon = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_icon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_icon.setIcon(icon2)
        self.pushButton_hello_icon.setIconSize(QtCore.QSize(253, 253))
        self.pushButton_hello_icon.setObjectName("pushButton_hello_icon")
        self.gridLayout_6.addWidget(self.pushButton_hello_icon, 0, 0, 6, 1)
        self.pushButton_hello_line = QtWidgets.QPushButton(self.widget_hello)
        self.pushButton_hello_line.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/hello/images/Hello_Line_Vertical.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_hello_line.setIcon(icon3)
        self.pushButton_hello_line.setIconSize(QtCore.QSize(21, 253))
        self.pushButton_hello_line.setObjectName("pushButton_hello_line")
        self.gridLayout_6.addWidget(self.pushButton_hello_line, 0, 1, 6, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem16, 5, 2, 1, 3)
        self.gridLayout_5.addWidget(self.widget_hello, 1, 1, 1, 1)
        self.stackedWidget_main.addWidget(self.page_hello)
        self.horizontalLayout_2.addWidget(self.stackedWidget_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_main.setCurrentIndex(1)
        self.stackedWidget_main_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOS Ⅲ 启动器"))
        self.label_Sidebar_Back.setToolTip(_translate("MainWindow", "返回"))
        self.label_Sidebar_User.setToolTip(_translate("MainWindow", "用户"))
        self.label_Sidebar_Home.setToolTip(_translate("MainWindow", "主页"))
        self.label_Sidebar_OnLine.setToolTip(_translate("MainWindow", "联机"))
        self.label_Sidebar_Download.setToolTip(_translate("MainWindow", "下载"))
        self.label_Sidebar_Settings.setToolTip(_translate("MainWindow", "设置"))
        self.label_page_settings_h1.setText(_translate("MainWindow", "个性化外观设置"))
        self.label_page_settings_subject_h2.setText(_translate("MainWindow", "主题"))
        self.radioButton_settings_subject_light.setToolTip(_translate("MainWindow", "浅色模式"))
        self.radioButton_settings_subject_light.setText(_translate("MainWindow", "浅色"))
        self.radioButton_settings_subject_dark.setToolTip(_translate("MainWindow", "深色模式"))
        self.radioButton_settings_subject_dark.setText(_translate("MainWindow", "深色"))
        self.radioButton_settings_subject_automatic.setToolTip(_translate("MainWindow", "跟随系统(只限于Mac系统)"))
        self.radioButton_settings_subject_automatic.setText(_translate("MainWindow", "跟随系统"))
        self.radioButton_settings_background_none.setText(_translate("MainWindow", "无"))
        self.radioButton_settings_background_1.setText(_translate("MainWindow", "清爽橙黄"))
        self.radioButton_settings_background_2.setText(_translate("MainWindow", "梦幻浅蓝"))
        self.radioButton_settings_background_3.setText(_translate("MainWindow", "梦幻浅红"))
        self.radioButton_settings_background_4.setText(_translate("MainWindow", "三彩斑斓"))
        self.radioButton_settings_background_5.setText(_translate("MainWindow", "深蓝天空"))
        self.radioButton_settings_background_6.setText(_translate("MainWindow", "蓝白相照"))
        self.radioButton_settings_background_7.setText(_translate("MainWindow", "粉色迷雾"))
        self.label_page_settings_background_h2.setText(_translate("MainWindow", "背景"))
        self.label_page_settings_background_h3.setText(_translate("MainWindow", "每帧间隔 (毫秒-mm)："))
        self.label_page_settings_sidebar_h2.setText(_translate("MainWindow", "左边栏动画设置"))
        self.spinBox_page_settings_sidebar.setSuffix(_translate("MainWindow", " mm"))
        self.label_page_settings_background_h3_2.setText(_translate("MainWindow", "预计 450mm (0.45s)完成"))
        self.label_loading_text_1.setText(_translate("MainWindow", "正在初始化启动器……"))
        self.label_loading_text_2.setText(_translate("MainWindow", "正在读取设置(1/3)"))
from UI.Custom_UI.QLabel import MyQLabel
