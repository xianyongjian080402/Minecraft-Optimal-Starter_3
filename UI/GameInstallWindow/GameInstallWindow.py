# Form implementation generated from reading ui file 'GameInstallWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_GameInstall(object):
    def setupUi(self, Dialog_GameInstall):
        Dialog_GameInstall.setObjectName("Dialog_GameInstall")
        Dialog_GameInstall.resize(585, 240)
        Dialog_GameInstall.setStyleSheet("QProgressBar{\n"
"    text-align: center;\n"
"    border-style:none;\n"
"    border-radius:5px;\n"
"    background-color: rgb(245, 245, 245);\n"
"    height:10px;\n"
"    color: rgb(66, 66, 66);\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius:5px;\n"
"    background-color: rgb(26, 135, 255);\n"
"}\n"
"\n"
"\n"
"#widget_main{\n"
"    border: 1px solid rgb(33, 33, 33);\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#widget_up{\n"
"    background-color: rgb(248, 248, 248);\n"
"    border: 1px solid rgba(0, 0, 0,0);\n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;\n"
"}\n"
"\n"
"#widget_bottom > QPushButton{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#scrollArea,\n"
"#stackedWidget,\n"
"#stackedWidget > QWidget,\n"
"#scrollAreaWidgetContents{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog_GameInstall)
        self.horizontalLayout.setContentsMargins(6, 4, 10, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_main = QtWidgets.QWidget(Dialog_GameInstall)
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_up = QtWidgets.QWidget(self.widget_main)
        self.widget_up.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_up.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_up.setObjectName("widget_up")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_up)
        self.gridLayout.setContentsMargins(12, 0, -1, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 2, 1)
        self.label = QtWidgets.QLabel(self.widget_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.label_4 = MyQLabel(self.widget_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(18, 18))
        self.label_4.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/image/images/PopUpWindow.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setIndent(5)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 2, 1)
        self.verticalLayout_2.addWidget(self.widget_up)
        self.widget_middle = QtWidgets.QWidget(self.widget_main)
        self.widget_middle.setObjectName("widget_middle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_middle)
        self.horizontalLayout_3.setContentsMargins(19, 5, 19, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_middle)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_widget_middle_start = QtWidgets.QWidget()
        self.page_widget_middle_start.setObjectName("page_widget_middle_start")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_widget_middle_start)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.page_widget_middle_start)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.progressBar_start = QtWidgets.QProgressBar(self.page_widget_middle_start)
        self.progressBar_start.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar_start.setMinimum(0)
        self.progressBar_start.setMaximum(0)
        self.progressBar_start.setProperty("value", 0)
        self.progressBar_start.setTextVisible(False)
        self.progressBar_start.setObjectName("progressBar_start")
        self.verticalLayout_3.addWidget(self.progressBar_start)
        spacerItem1 = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page_widget_middle_start)
        self.page_widget_middle_inatall = QtWidgets.QWidget()
        self.page_widget_middle_inatall.setObjectName("page_widget_middle_inatall")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_widget_middle_inatall)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_widget_middle_inatall)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 527, 131))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_inatall_Jar = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_inatall_Jar.setFont(font)
        self.label_inatall_Jar.setObjectName("label_inatall_Jar")
        self.verticalLayout.addWidget(self.label_inatall_Jar)
        self.progressBar_inatall_Jar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_inatall_Jar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar_inatall_Jar.setMinimum(0)
        self.progressBar_inatall_Jar.setMaximum(0)
        self.progressBar_inatall_Jar.setProperty("value", 0)
        self.progressBar_inatall_Jar.setTextVisible(False)
        self.progressBar_inatall_Jar.setObjectName("progressBar_inatall_Jar")
        self.verticalLayout.addWidget(self.progressBar_inatall_Jar)
        self.label_inatall_assetsFile = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_inatall_assetsFile.setFont(font)
        self.label_inatall_assetsFile.setObjectName("label_inatall_assetsFile")
        self.verticalLayout.addWidget(self.label_inatall_assetsFile)
        self.progressBar_inatall_assetsFile = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_inatall_assetsFile.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar_inatall_assetsFile.setMaximum(100)
        self.progressBar_inatall_assetsFile.setProperty("value", 0)
        self.progressBar_inatall_assetsFile.setTextVisible(False)
        self.progressBar_inatall_assetsFile.setObjectName("progressBar_inatall_assetsFile")
        self.verticalLayout.addWidget(self.progressBar_inatall_assetsFile)
        self.label_inatall_libraryFile = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_inatall_libraryFile.setFont(font)
        self.label_inatall_libraryFile.setObjectName("label_inatall_libraryFile")
        self.verticalLayout.addWidget(self.label_inatall_libraryFile)
        self.progressBar_inatall_libraryFile = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_inatall_libraryFile.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar_inatall_libraryFile.setMaximum(100)
        self.progressBar_inatall_libraryFile.setProperty("value", 0)
        self.progressBar_inatall_libraryFile.setTextVisible(False)
        self.progressBar_inatall_libraryFile.setObjectName("progressBar_inatall_libraryFile")
        self.verticalLayout.addWidget(self.progressBar_inatall_libraryFile)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_widget_middle_inatall)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.widget_middle)
        self.widget_bottom = QtWidgets.QWidget(self.widget_main)
        self.widget_bottom.setObjectName("widget_bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_bottom)
        self.horizontalLayout_4.setContentsMargins(19, 17, 19, 15)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_info_spend = QtWidgets.QLabel(self.widget_bottom)
        self.label_info_spend.setObjectName("label_info_spend")
        self.horizontalLayout_4.addWidget(self.label_info_spend)
        self.label_info_size = QtWidgets.QLabel(self.widget_bottom)
        self.label_info_size.setObjectName("label_info_size")
        self.horizontalLayout_4.addWidget(self.label_info_size)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_bottom_cancel = QtWidgets.QPushButton(self.widget_bottom)
        self.pushButton_bottom_cancel.setMinimumSize(QtCore.QSize(26, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_bottom_cancel.setFont(font)
        self.pushButton_bottom_cancel.setAutoDefault(False)
        self.pushButton_bottom_cancel.setObjectName("pushButton_bottom_cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_bottom_cancel)
        self.verticalLayout_2.addWidget(self.widget_bottom)
        self.horizontalLayout.addWidget(self.widget_main)

        self.retranslateUi(Dialog_GameInstall)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_GameInstall)

    def retranslateUi(self, Dialog_GameInstall):
        _translate = QtCore.QCoreApplication.translate
        Dialog_GameInstall.setWindowTitle(_translate("Dialog_GameInstall", "Dialog"))
        self.label.setText(_translate("Dialog_GameInstall", "安装游戏"))
        self.label_8.setText(_translate("Dialog_GameInstall", "准备安装"))
        self.label_inatall_Jar.setText(_translate("Dialog_GameInstall", "原版Jar下载"))
        self.label_inatall_assetsFile.setText(_translate("Dialog_GameInstall", "游戏资源文件下载 (方式A)"))
        self.label_inatall_libraryFile.setText(_translate("Dialog_GameInstall", "游戏支持库文件下载+安装"))
        self.label_info_spend.setText(_translate("Dialog_GameInstall", "0MB/s"))
        self.label_info_size.setText(_translate("Dialog_GameInstall", "0MB/???MB"))
        self.pushButton_bottom_cancel.setText(_translate("Dialog_GameInstall", "取消"))
from UI.Custom_UI.QLabel import MyQLabel
