# Form implementation generated from reading ui file 'AddUserWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AddUserWindows(object):
    def setupUi(self, Dialog_AddUserWindows):
        Dialog_AddUserWindows.setObjectName("Dialog_AddUserWindows")
        Dialog_AddUserWindows.resize(585, 180)
        Dialog_AddUserWindows.setMinimumSize(QtCore.QSize(585, 180))
        Dialog_AddUserWindows.setMaximumSize(QtCore.QSize(585, 220))
        Dialog_AddUserWindows.setStyleSheet("*{\n"
"    padding: -1;  /*改变焦点框*/\n"
"}\n"
"\n"
"#Dialog_AddUserWindows{\n"
"    /*border-image: url(:/Shadow/images/Shadow-2-4-6-2.png);*/\n"
"    border-radius: 8px;\n"
"}\n"
"#stackedWidget_main > QWidget{\n"
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
"#widget_up_2 > QLabel{\n"
"    color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"#pushButton_OffLine_Advanced{\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#widget_bottom > QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#pushButton_bottom_cancel_confirm{\n"
"    color: rgb(0, 119, 255);\n"
"}\n"
"\n"
"#widget_main{\n"
"    border: 1px solid rgb(33, 33, 33);\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#widget_2{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgba(204, 204, 255, 26);\n"
"    border-style:none;\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_AddUserWindows)
        self.verticalLayout.setContentsMargins(6, 4, 10, 11)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_main = QtWidgets.QWidget(Dialog_AddUserWindows)
        self.widget_main.setObjectName("widget_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 12)
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
        self.widget_up_2 = QtWidgets.QWidget(self.widget_up)
        self.widget_up_2.setObjectName("widget_up_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_up_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = MyQLabel(self.widget_up_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 119, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_2.setIndent(5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = MyQLabel(self.widget_up_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3.setIndent(5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = MyQLabel(self.widget_up_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4.setIndent(5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.gridLayout.addWidget(self.widget_up_2, 0, 3, 4, 1)
        self.label = QtWidgets.QLabel(self.widget_up)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 4, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 4, 2)
        self.verticalLayout_2.addWidget(self.widget_up)
        self.stackedWidget_main = QtWidgets.QStackedWidget(self.widget_main)
        self.stackedWidget_main.setObjectName("stackedWidget_main")
        self.page_OffLine = QtWidgets.QWidget()
        self.page_OffLine.setObjectName("page_OffLine")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_OffLine)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_OffLine_1 = QtWidgets.QWidget(self.page_OffLine)
        self.widget_OffLine_1.setObjectName("widget_OffLine_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_OffLine_1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_OffLine_1)
        self.label_5.setMinimumSize(QtCore.QSize(55, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_OffLine = QtWidgets.QLineEdit(self.widget_OffLine_1)
        self.lineEdit_OffLine.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_OffLine.setFont(font)
        self.lineEdit_OffLine.setClearButtonEnabled(False)
        self.lineEdit_OffLine.setObjectName("lineEdit_OffLine")
        self.horizontalLayout_3.addWidget(self.lineEdit_OffLine)
        self.gridLayout_2.addWidget(self.widget_OffLine_1, 1, 0, 1, 3)
        self.stackedWidget_OffLine_widget_2 = QtWidgets.QStackedWidget(self.page_OffLine)
        self.stackedWidget_OffLine_widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget_OffLine_widget_2.setMaximumSize(QtCore.QSize(16777215, 0))
        self.stackedWidget_OffLine_widget_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.stackedWidget_OffLine_widget_2.setObjectName("stackedWidget_OffLine_widget_2")
        self.page_widget_2 = QtWidgets.QWidget()
        self.page_widget_2.setObjectName("page_widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_OffLine_2 = QtWidgets.QWidget(self.page_widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_OffLine_2.sizePolicy().hasHeightForWidth())
        self.widget_OffLine_2.setSizePolicy(sizePolicy)
        self.widget_OffLine_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_OffLine_2.setObjectName("widget_OffLine_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_OffLine_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget_OffLine_2)
        self.label_6.setMinimumSize(QtCore.QSize(55, 38))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit_OffLine_Advanced = QtWidgets.QLineEdit(self.widget_OffLine_2)
        self.lineEdit_OffLine_Advanced.setEnabled(False)
        self.lineEdit_OffLine_Advanced.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_OffLine_Advanced.setFont(font)
        self.lineEdit_OffLine_Advanced.setObjectName("lineEdit_OffLine_Advanced")
        self.horizontalLayout.addWidget(self.lineEdit_OffLine_Advanced)
        self.horizontalLayout_5.addWidget(self.widget_OffLine_2)
        self.stackedWidget_OffLine_widget_2.addWidget(self.page_widget_2)
        self.page_2_widget_2 = QtWidgets.QWidget()
        self.page_2_widget_2.setObjectName("page_2_widget_2")
        self.stackedWidget_OffLine_widget_2.addWidget(self.page_2_widget_2)
        self.gridLayout_2.addWidget(self.stackedWidget_OffLine_widget_2, 5, 0, 1, 3)
        self.pushButton_OffLine_Advanced = QtWidgets.QPushButton(self.page_OffLine)
        self.pushButton_OffLine_Advanced.setEnabled(True)
        self.pushButton_OffLine_Advanced.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_OffLine_Advanced.setMaximumSize(QtCore.QSize(70, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_OffLine_Advanced.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/widget_Sidebar/images/TriangleUp.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_OffLine_Advanced.setIcon(icon)
        self.pushButton_OffLine_Advanced.setIconSize(QtCore.QSize(13, 7))
        self.pushButton_OffLine_Advanced.setChecked(False)
        self.pushButton_OffLine_Advanced.setAutoDefault(False)
        self.pushButton_OffLine_Advanced.setObjectName("pushButton_OffLine_Advanced")
        self.gridLayout_2.addWidget(self.pushButton_OffLine_Advanced, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 3)
        self.stackedWidget_main.addWidget(self.page_OffLine)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget_main.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_main.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget_main)
        self.widget_bottom = QtWidgets.QWidget(self.widget_main)
        self.widget_bottom.setObjectName("widget_bottom")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_bottom)
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_bottom_cancel = QtWidgets.QPushButton(self.widget_bottom)
        self.pushButton_bottom_cancel.setMinimumSize(QtCore.QSize(26, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_bottom_cancel.setFont(font)
        self.pushButton_bottom_cancel.setAutoDefault(False)
        self.pushButton_bottom_cancel.setObjectName("pushButton_bottom_cancel")
        self.horizontalLayout_4.addWidget(self.pushButton_bottom_cancel)
        self.pushButton_bottom_cancel_confirm = QtWidgets.QPushButton(self.widget_bottom)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_bottom_cancel_confirm.setFont(font)
        self.pushButton_bottom_cancel_confirm.setAutoDefault(False)
        self.pushButton_bottom_cancel_confirm.setObjectName("pushButton_bottom_cancel_confirm")
        self.horizontalLayout_4.addWidget(self.pushButton_bottom_cancel_confirm)
        self.verticalLayout_2.addWidget(self.widget_bottom)
        self.verticalLayout.addWidget(self.widget_main)

        self.retranslateUi(Dialog_AddUserWindows)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_OffLine_widget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddUserWindows)

    def retranslateUi(self, Dialog_AddUserWindows):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddUserWindows.setWindowTitle(_translate("Dialog_AddUserWindows", "添加用户"))
        self.label_2.setText(_translate("Dialog_AddUserWindows", "离线账户"))
        self.label_3.setText(_translate("Dialog_AddUserWindows", "微软账户"))
        self.label_4.setText(_translate("Dialog_AddUserWindows", "第三方账户"))
        self.label.setText(_translate("Dialog_AddUserWindows", "添加用户"))
        self.label_5.setText(_translate("Dialog_AddUserWindows", "用户名"))
        self.lineEdit_OffLine.setPlaceholderText(_translate("Dialog_AddUserWindows", " XXX"))
        self.label_6.setText(_translate("Dialog_AddUserWindows", "UUID"))
        self.lineEdit_OffLine_Advanced.setPlaceholderText(_translate("Dialog_AddUserWindows", " XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"))
        self.pushButton_OffLine_Advanced.setText(_translate("Dialog_AddUserWindows", "高级设置"))
        self.pushButton_bottom_cancel.setText(_translate("Dialog_AddUserWindows", "取消"))
        self.pushButton_bottom_cancel_confirm.setText(_translate("Dialog_AddUserWindows", "登陆"))
from UI.Custom_UI.QLabel import MyQLabel
