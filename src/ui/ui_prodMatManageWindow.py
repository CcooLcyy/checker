# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\prodMatManageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prodMatManageWindow(object):
    def setupUi(self, prodMatManageWindow):
        prodMatManageWindow.setObjectName("prodMatManageWindow")
        prodMatManageWindow.resize(800, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(prodMatManageWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toMainWindowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.toMainWindowButton.setObjectName("toMainWindowButton")
        self.horizontalLayout_3.addWidget(self.toMainWindowButton)
        self.line_3 = QtWidgets.QFrame(prodMatManageWindow)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.toDataWindowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.toDataWindowButton.setObjectName("toDataWindowButton")
        self.horizontalLayout_3.addWidget(self.toDataWindowButton)
        self.toStateWindowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.toStateWindowButton.setObjectName("toStateWindowButton")
        self.horizontalLayout_3.addWidget(self.toStateWindowButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(prodMatManageWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createProductRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.createProductRowButton.setObjectName("createProductRowButton")
        self.horizontalLayout.addWidget(self.createProductRowButton)
        self.deleteProductRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.deleteProductRowButton.setObjectName("deleteProductRowButton")
        self.horizontalLayout.addWidget(self.deleteProductRowButton)
        self.addMatToProdButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.addMatToProdButton.setObjectName("addMatToProdButton")
        self.horizontalLayout.addWidget(self.addMatToProdButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.productShowTable = QtWidgets.QTableWidget(prodMatManageWindow)
        self.productShowTable.setGridStyle(QtCore.Qt.SolidLine)
        self.productShowTable.setWordWrap(True)
        self.productShowTable.setCornerButtonEnabled(True)
        self.productShowTable.setRowCount(0)
        self.productShowTable.setColumnCount(2)
        self.productShowTable.setObjectName("productShowTable")
        item = QtWidgets.QTableWidgetItem()
        self.productShowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productShowTable.setHorizontalHeaderItem(1, item)
        self.productShowTable.horizontalHeader().setVisible(True)
        self.productShowTable.horizontalHeader().setDefaultSectionSize(300)
        self.productShowTable.horizontalHeader().setSortIndicatorShown(True)
        self.productShowTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.productShowTable)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveProductRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.saveProductRowButton.setObjectName("saveProductRowButton")
        self.horizontalLayout_4.addWidget(self.saveProductRowButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(prodMatManageWindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createMaterialRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.createMaterialRowButton.setObjectName("createMaterialRowButton")
        self.horizontalLayout_2.addWidget(self.createMaterialRowButton)
        self.deleteMaterialRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.deleteMaterialRowButton.setObjectName("deleteMaterialRowButton")
        self.horizontalLayout_2.addWidget(self.deleteMaterialRowButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.materialShowTable = QtWidgets.QTableWidget(prodMatManageWindow)
        self.materialShowTable.setObjectName("materialShowTable")
        self.materialShowTable.setColumnCount(2)
        self.materialShowTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.materialShowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.materialShowTable.setHorizontalHeaderItem(1, item)
        self.materialShowTable.horizontalHeader().setDefaultSectionSize(300)
        self.materialShowTable.horizontalHeader().setHighlightSections(True)
        self.materialShowTable.horizontalHeader().setSortIndicatorShown(True)
        self.materialShowTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.materialShowTable)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saveMaterialRowButton = QtWidgets.QPushButton(prodMatManageWindow)
        self.saveMaterialRowButton.setObjectName("saveMaterialRowButton")
        self.horizontalLayout_5.addWidget(self.saveMaterialRowButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(prodMatManageWindow)
        QtCore.QMetaObject.connectSlotsByName(prodMatManageWindow)

    def retranslateUi(self, prodMatManageWindow):
        _translate = QtCore.QCoreApplication.translate
        prodMatManageWindow.setWindowTitle(_translate("prodMatManageWindow", "产品物料管理"))
        self.toMainWindowButton.setText(_translate("prodMatManageWindow", "返回主界面"))
        self.toDataWindowButton.setText(_translate("prodMatManageWindow", "数据处理"))
        self.toStateWindowButton.setText(_translate("prodMatManageWindow", "数据统计"))
        self.createProductRowButton.setText(_translate("prodMatManageWindow", "新建产品"))
        self.deleteProductRowButton.setText(_translate("prodMatManageWindow", "删除产品"))
        self.addMatToProdButton.setText(_translate("prodMatManageWindow", "向产品添加物料"))
        self.productShowTable.setSortingEnabled(True)
        item = self.productShowTable.horizontalHeaderItem(0)
        item.setText(_translate("prodMatManageWindow", "产品ID"))
        item = self.productShowTable.horizontalHeaderItem(1)
        item.setText(_translate("prodMatManageWindow", "产品名称"))
        self.saveProductRowButton.setText(_translate("prodMatManageWindow", "保存"))
        self.createMaterialRowButton.setText(_translate("prodMatManageWindow", "新建物料"))
        self.deleteMaterialRowButton.setText(_translate("prodMatManageWindow", "删除物料"))
        self.materialShowTable.setSortingEnabled(True)
        item = self.materialShowTable.horizontalHeaderItem(0)
        item.setText(_translate("prodMatManageWindow", "物料ID"))
        item = self.materialShowTable.horizontalHeaderItem(1)
        item.setText(_translate("prodMatManageWindow", "物料名称"))
        self.saveMaterialRowButton.setText(_translate("prodMatManageWindow", "保存"))
