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
        mainWindow.resize(1000, 800)
        mainWindow.setMinimumSize(QtCore.QSize(1000, 800))
        mainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.gridLayout_3 = QtWidgets.QGridLayout(mainWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.changeUserButton = QtWidgets.QPushButton(mainWindow)
        self.changeUserButton.setObjectName("changeUserButton")
        self.horizontalLayout.addWidget(self.changeUserButton, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toDataWindowButton = QtWidgets.QPushButton(mainWindow)
        self.toDataWindowButton.setObjectName("toDataWindowButton")
        self.gridLayout_2.addWidget(self.toDataWindowButton, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "主界面"))
        self.changeUserButton.setText(_translate("mainWindow", "切换用户"))
        self.toDataWindowButton.setText(_translate("mainWindow", "数据处理"))
