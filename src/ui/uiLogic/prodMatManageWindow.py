from PyQt5 import QtWidgets, QtCore
import sys, os
sys.path.append('src')
from func.mysql import Mysql
from ui.ui_prodMatManageWindow import Ui_prodMatManageWindow
from ui.uiLogic.addMaterialWindow import AddMaterialWindow

class prodMatManageWindow(QtWidgets.QWidget, Ui_prodMatManageWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toDataWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sql = Mysql()
        self.alterProdRow = []
        self.alterMatRow = []
        self.__initProdRow()
        self.__initMatRow()
        self.productShowTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.createProductRowButton.clicked.connect(self.createProductRowSlot)
        self.createMaterialRowButton.clicked.connect(self.createMaterialRowSlot)
        self.deleteProductRowButton.clicked.connect(self.deleteProductRowSlot)
        self.deleteMaterialRowButton.clicked.connect(self.deleteMaterialRowSlot)
        self.addMatToProdButton.clicked.connect(self.addMatToProdSlot)
        self.saveProductRowButton.clicked.connect(self.saveProductRowSlot)

    def __initProdRow(self):
        result = self.sql.queryAllProduct()
        self.productShowTable.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.productShowTable.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.productShowTable.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            self.alterProdRow.append(row)
            itemRow += 1

    def __initMatRow(self):
        result = self.sql.queryAllProduct()
        self.productShowTable.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.productShowTable.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.productShowTable.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            self.alterMatRow.append(row)
            itemRow += 1

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

    def createProductRowSlot(self):
        row = self.productShowTable.rowCount()
        self.productShowTable.insertRow(row)

    def deleteProductRowSlot(self):
        selectedIndexes = self.productShowTable.selectionModel().selectedRows()
        for index in sorted(selectedIndexes, reverse=True):
            self.productShowTable.removeRow(index.row())

    def createMaterialRowSlot(self):
        row = self.materialShowTable.rowCount()
        self.materialShowTable.insertRow(row)

    def deleteMaterialRowSlot(self):
        selectedIndexes = self.materialShowTable.selectionModel().selectedRows()
        for index in sorted(selectedIndexes, reverse=True):
            self.materialShowTable.removeRow(index.row())

    def addMatToProdSlot(self):
        self.addMatToProdWindow = AddMaterialWindow()
        self.addMatToProdWindow.show()

    def saveProductRowSlot(self):
        pass