# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\manageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manageWindow(object):
    def setupUi(self, manageWindow):
        manageWindow.setObjectName("manageWindow")
        manageWindow.resize(800, 640)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(manageWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.changeUserButton = QtWidgets.QPushButton(manageWindow)
        self.changeUserButton.setObjectName("changeUserButton")
        self.verticalLayout_3.addWidget(self.changeUserButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(manageWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(manageWindow)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.addUserButton = QtWidgets.QPushButton(manageWindow)
        self.addUserButton.setObjectName("addUserButton")
        self.verticalLayout.addWidget(self.addUserButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(manageWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.addUserNameEdit = QtWidgets.QLineEdit(manageWindow)
        self.addUserNameEdit.setAccessibleDescription("")
        self.addUserNameEdit.setStyleSheet("")
        self.addUserNameEdit.setInputMask("")
        self.addUserNameEdit.setObjectName("addUserNameEdit")
        self.horizontalLayout.addWidget(self.addUserNameEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(manageWindow)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.addUserPasswordEdit = QtWidgets.QLineEdit(manageWindow)
        self.addUserPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.addUserPasswordEdit.setObjectName("addUserPasswordEdit")
        self.horizontalLayout_2.addWidget(self.addUserPasswordEdit)
        self.label_10 = QtWidgets.QLabel(manageWindow)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.addUserPasswordReEdit = QtWidgets.QLineEdit(manageWindow)
        self.addUserPasswordReEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.addUserPasswordReEdit.setObjectName("addUserPasswordReEdit")
        self.horizontalLayout_2.addWidget(self.addUserPasswordReEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(manageWindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(manageWindow)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.changePasswordButton = QtWidgets.QPushButton(manageWindow)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.verticalLayout.addWidget(self.changePasswordButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(manageWindow)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.changeUserNameEdit = QtWidgets.QLineEdit(manageWindow)
        self.changeUserNameEdit.setObjectName("changeUserNameEdit")
        self.horizontalLayout_3.addWidget(self.changeUserNameEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(manageWindow)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.changeUserPasswordEdit = QtWidgets.QLineEdit(manageWindow)
        self.changeUserPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changeUserPasswordEdit.setObjectName("changeUserPasswordEdit")
        self.horizontalLayout_4.addWidget(self.changeUserPasswordEdit)
        self.label_9 = QtWidgets.QLabel(manageWindow)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.changeUserPasswordReEdit = QtWidgets.QLineEdit(manageWindow)
        self.changeUserPasswordReEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.changeUserPasswordReEdit.setObjectName("changeUserPasswordReEdit")
        self.horizontalLayout_4.addWidget(self.changeUserPasswordReEdit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(manageWindow)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(manageWindow)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.queryUserButton = QtWidgets.QPushButton(manageWindow)
        self.queryUserButton.setObjectName("queryUserButton")
        self.horizontalLayout_5.addWidget(self.queryUserButton)
        self.deleteUserButton = QtWidgets.QPushButton(manageWindow)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.horizontalLayout_5.addWidget(self.deleteUserButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(manageWindow)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.deleteUserEdit = QtWidgets.QLineEdit(manageWindow)
        self.deleteUserEdit.setObjectName("deleteUserEdit")
        self.horizontalLayout_6.addWidget(self.deleteUserEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.line_5 = QtWidgets.QFrame(manageWindow)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.line_4 = QtWidgets.QFrame(manageWindow)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_7.addWidget(self.line_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clearManageInfoShowButton = QtWidgets.QPushButton(manageWindow)
        self.clearManageInfoShowButton.setObjectName("clearManageInfoShowButton")
        self.verticalLayout_2.addWidget(self.clearManageInfoShowButton, 0, QtCore.Qt.AlignRight)
        self.line_6 = QtWidgets.QFrame(manageWindow)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.manageInfoShow = QtWidgets.QPlainTextEdit(manageWindow)
        self.manageInfoShow.setObjectName("manageInfoShow")
        self.verticalLayout_2.addWidget(self.manageInfoShow)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.retranslateUi(manageWindow)
        QtCore.QMetaObject.connectSlotsByName(manageWindow)
        manageWindow.setTabOrder(self.changeUserButton, self.addUserNameEdit)
        manageWindow.setTabOrder(self.addUserNameEdit, self.addUserPasswordEdit)
        manageWindow.setTabOrder(self.addUserPasswordEdit, self.addUserPasswordReEdit)
        manageWindow.setTabOrder(self.addUserPasswordReEdit, self.addUserButton)
        manageWindow.setTabOrder(self.addUserButton, self.changeUserNameEdit)
        manageWindow.setTabOrder(self.changeUserNameEdit, self.changeUserPasswordEdit)
        manageWindow.setTabOrder(self.changeUserPasswordEdit, self.changeUserPasswordReEdit)
        manageWindow.setTabOrder(self.changeUserPasswordReEdit, self.changePasswordButton)
        manageWindow.setTabOrder(self.changePasswordButton, self.queryUserButton)
        manageWindow.setTabOrder(self.queryUserButton, self.deleteUserEdit)
        manageWindow.setTabOrder(self.deleteUserEdit, self.deleteUserButton)
        manageWindow.setTabOrder(self.deleteUserButton, self.clearManageInfoShowButton)
        manageWindow.setTabOrder(self.clearManageInfoShowButton, self.manageInfoShow)

    def retranslateUi(self, manageWindow):
        _translate = QtCore.QCoreApplication.translate
        manageWindow.setWindowTitle(_translate("manageWindow", "管理界面"))
        self.changeUserButton.setText(_translate("manageWindow", "切换用户"))
        self.label_5.setText(_translate("manageWindow", "添加用户"))
        self.addUserButton.setText(_translate("manageWindow", "添加用户"))
        self.label_2.setText(_translate("manageWindow", "用户名"))
        self.addUserNameEdit.setPlaceholderText(_translate("manageWindow", "用户名"))
        self.label.setText(_translate("manageWindow", "密码"))
        self.addUserPasswordEdit.setPlaceholderText(_translate("manageWindow", "密码"))
        self.label_10.setText(_translate("manageWindow", "重复密码"))
        self.addUserPasswordReEdit.setPlaceholderText(_translate("manageWindow", "重复密码"))
        self.label_6.setText(_translate("manageWindow", "修改用户密码"))
        self.changePasswordButton.setText(_translate("manageWindow", "更改密码"))
        self.label_4.setText(_translate("manageWindow", "用户名"))
        self.changeUserNameEdit.setPlaceholderText(_translate("manageWindow", "用户名"))
        self.label_3.setText(_translate("manageWindow", "新密码"))
        self.changeUserPasswordEdit.setPlaceholderText(_translate("manageWindow", "新密码"))
        self.label_9.setText(_translate("manageWindow", "重复密码"))
        self.changeUserPasswordReEdit.setPlaceholderText(_translate("manageWindow", "重复新密码"))
        self.label_7.setText(_translate("manageWindow", "删除用户"))
        self.queryUserButton.setText(_translate("manageWindow", "查询用户"))
        self.deleteUserButton.setText(_translate("manageWindow", "删除用户"))
        self.label_8.setText(_translate("manageWindow", "待删除用户名"))
        self.deleteUserEdit.setPlaceholderText(_translate("manageWindow", "用户名"))
        self.clearManageInfoShowButton.setText(_translate("manageWindow", "清除信息"))
