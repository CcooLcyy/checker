# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\changeLocalUserPasswordWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeLocalUserPassword(object):
    def setupUi(self, changeLocalUserPassword):
        changeLocalUserPassword.setObjectName("changeLocalUserPassword")
        changeLocalUserPassword.resize(318, 189)
        changeLocalUserPassword.setMinimumSize(QtCore.QSize(318, 189))
        changeLocalUserPassword.setMaximumSize(QtCore.QSize(318, 189))
        self.verticalLayout = QtWidgets.QVBoxLayout(changeLocalUserPassword)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(changeLocalUserPassword)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.userNameShow = QtWidgets.QLabel(changeLocalUserPassword)
        self.userNameShow.setObjectName("userNameShow")
        self.horizontalLayout_5.addWidget(self.userNameShow)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(changeLocalUserPassword)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.oldPassword = QtWidgets.QLineEdit(changeLocalUserPassword)
        self.oldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPassword.setObjectName("oldPassword")
        self.horizontalLayout.addWidget(self.oldPassword)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(changeLocalUserPassword)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.newPassword = QtWidgets.QLineEdit(changeLocalUserPassword)
        self.newPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword.setObjectName("newPassword")
        self.horizontalLayout_2.addWidget(self.newPassword)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(changeLocalUserPassword)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.newPasswordRe = QtWidgets.QLineEdit(changeLocalUserPassword)
        self.newPasswordRe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordRe.setObjectName("newPasswordRe")
        self.horizontalLayout_3.addWidget(self.newPasswordRe)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.changePasswordButton = QtWidgets.QPushButton(changeLocalUserPassword)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.horizontalLayout_4.addWidget(self.changePasswordButton)
        self.cancelButton = QtWidgets.QPushButton(changeLocalUserPassword)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(changeLocalUserPassword)
        QtCore.QMetaObject.connectSlotsByName(changeLocalUserPassword)

    def retranslateUi(self, changeLocalUserPassword):
        _translate = QtCore.QCoreApplication.translate
        changeLocalUserPassword.setWindowTitle(_translate("changeLocalUserPassword", "修改用户密码"))
        self.label.setText(_translate("changeLocalUserPassword", "登录用户"))
        self.userNameShow.setText(_translate("changeLocalUserPassword", "\"用户名\""))
        self.label_3.setText(_translate("changeLocalUserPassword", "旧密码"))
        self.oldPassword.setPlaceholderText(_translate("changeLocalUserPassword", "旧密码"))
        self.label_4.setText(_translate("changeLocalUserPassword", "新密码"))
        self.newPassword.setPlaceholderText(_translate("changeLocalUserPassword", "新密码"))
        self.label_5.setText(_translate("changeLocalUserPassword", "重复密码"))
        self.newPasswordRe.setPlaceholderText(_translate("changeLocalUserPassword", "重复新密码"))
        self.changePasswordButton.setText(_translate("changeLocalUserPassword", "确定"))
        self.cancelButton.setText(_translate("changeLocalUserPassword", "取消"))
