# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 640)
        self.groupBox = QtWidgets.QGroupBox(mainWindow)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 782, 593))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.toDataWindowButton = QtWidgets.QPushButton(self.groupBox)
        self.toDataWindowButton.setGeometry(QtCore.QRect(450, 240, 100, 100))
        self.toDataWindowButton.setObjectName("toDataWindowButton")
        self.productManageButton = QtWidgets.QPushButton(self.groupBox)
        self.productManageButton.setGeometry(QtCore.QRect(210, 240, 100, 100))
        self.productManageButton.setObjectName("productManageButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(340, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.changeUserButton = QtWidgets.QPushButton(mainWindow)
        self.changeUserButton.setGeometry(QtCore.QRect(9, 9, 75, 23))
        self.changeUserButton.setObjectName("changeUserButton")
        self.pushButton = QtWidgets.QPushButton(mainWindow)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "主界面"))
        self.toDataWindowButton.setText(_translate("mainWindow", "数据处理"))
        self.productManageButton.setText(_translate("mainWindow", "产品管理"))
        self.label.setText(_translate("mainWindow", "->"))
        self.changeUserButton.setText(_translate("mainWindow", "切换用户"))
        self.pushButton.setText(_translate("mainWindow", "修改密码"))
