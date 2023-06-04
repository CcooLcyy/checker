from PyQt5 import QtWidgets, QtCore, QtGui
import sys, os
sys.path.append('src')
from ui.ui_prodMatManageWindow import Ui_prodMatManageWindow
from ui.uiLogic.addMaterialWindow import AddMaterialWindow

class OnlyNum(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        validator = QtGui.QIntValidator()
        editor.setValidator(validator)
        return editor

class prodMatManageWindow(QtWidgets.QWidget, Ui_prodMatManageWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toDataWindowSignal = QtCore.pyqtSignal()
    toStateWindowSingal = QtCore.pyqtSignal()
    def __init__(self, sql):
        super().__init__()
        self.setupUi(self)

        self.sql = sql
        self.addProdRow = []
        self.addMatRow = []
        self.changeProdRow = []
        self.changeMatRow = []
        self.delProdRow = []
        self.delMatRow = []
        self.selectedValue = ''
        self.columnArray = []
        self.selectRowItemText = ''
        self.__initProdRow()
        self.__initMatRow()
        self.prodRowCount = self.productShowTable.rowCount()
        self.matRowCount = self.materialShowTable.rowCount()

        self.productShowTable.setItemDelegateForColumn(0, OnlyNum())
        self.materialShowTable.setItemDelegateForColumn(0, OnlyNum())
        self.productShowTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.materialShowTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.toStateWindowButton.clicked.connect(self.toStateWindowSlot)
        self.createProductRowButton.clicked.connect(self.createProductRowSlot)
        self.createMaterialRowButton.clicked.connect(self.createMaterialRowSlot)
        self.deleteProductRowButton.clicked.connect(self.deleteProductRowSlot)
        self.deleteMaterialRowButton.clicked.connect(self.deleteMaterialRowSlot)
        self.addMatToProdButton.clicked.connect(self.addMatToProdSlot)
        self.saveProductRowButton.clicked.connect(self.saveProductRowSlot)
        self.saveMaterialRowButton.clicked.connect(self.saveMaterialRowSlot)
        self.productShowTable.itemChanged.connect(self.addProdRowSlot)
        self.materialShowTable.itemChanged.connect(self.addMatRowSlot)
        self.productShowTable.cellDoubleClicked.connect(lambda: self.selectedValueSave(self.productShowTable))
        self.materialShowTable.cellDoubleClicked.connect(lambda: self.selectedValueSave(self.materialShowTable))
        self.productShowTable.itemClicked.connect(self.selectRowSlot)

    def __initProdRow(self):
        result = self.sql.queryAllProduct()
        self.productShowTable.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.productShowTable.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.productShowTable.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            self.addProdRow.append(row)
            itemRow += 1
        self.addProdRow = []

    def __initMatRow(self):
        result = self.sql.queryAllMaterial()
        self.materialShowTable.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.materialShowTable.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.materialShowTable.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            self.addMatRow.append(row)
            itemRow += 1
        self.addMatRow = []

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

    def toStateWindowSlot(self):
        self.toStateWindowSingal.emit()

    def createProductRowSlot(self):
        self.__createRow('prod', self.productShowTable)

    def createMaterialRowSlot(self):
        self.__createRow('mat', self.materialShowTable)

    def __createRow(self, type, tableWidgetName):
        row = tableWidgetName.rowCount()
        tableWidgetName.insertRow(row)
        if type == 'prod':
            self.prodRowCount = tableWidgetName.rowCount()
        elif type == 'mat':
            self.matRowCount = tableWidgetName.rowCount()

    def deleteProductRowSlot(self):
        self.__deleteRow(self.productShowTable, self.delProdRow)

    def deleteMaterialRowSlot(self):
        self.__deleteRow(self.materialShowTable, self.delMatRow)

    def __deleteRow(self, tableWidgetName, deleteRow):
        selectedIndexes = tableWidgetName.selectionModel().selectedRows()
        for index in sorted(selectedIndexes, reverse=True):
            item = tableWidgetName.item(index.row(), 0)
            if item:
                deleteRow.append(item.text())
            else:
                pass
            tableWidgetName.removeRow(index.row())

    def addProdRowSlot(self, item):
        self.__addProdMatRow(item, self.productShowTable, self.prodRowCount, self.delProdRow, self.changeProdRow, self.addProdRow)

    def addMatRowSlot(self, item):
        self.__addProdMatRow(item, self.materialShowTable, self.matRowCount, self.delMatRow, self.changeMatRow, self.addMatRow)

    def __addProdMatRow(self, item, tableWidgetName, rowCount, delRow, changeRow, addRow):
        row = item.row()
        rowFilled = True
        for column in range(tableWidgetName.columnCount()):
            if not tableWidgetName.item(row, column):
                rowFilled = False
                break
            if item.text() == '': 
                rowFilled = False
                break
            if tableWidgetName.item(row, 0).text() in self.columnArray:
                try:
                    if tableWidgetName.item(row, 1).text() != '':
                        break
                    else:
                        QtWidgets.QMessageBox.information(self, '警告', 'ID不能重复')
                        tableWidgetName.blockSignals(True)
                        tableWidgetName.setItem(row, 0, QtWidgets.QTableWidgetItem(self.selectedValue))
                        delRow.append(self.selectedValue)
                        tableWidgetName.blockSignals(False)
                        return
                except Exception as e:
                    QtWidgets.QMessageBox.information(self, '警告', 'ID不能重复')
                    tableWidgetName.blockSignals(True)
                    tableWidgetName.setItem(row, 0, QtWidgets.QTableWidgetItem(self.selectedValue))
                    tableWidgetName.blockSignals(False)
                    return
            if rowCount == tableWidgetName.rowCount():  
                if tableWidgetName.item(row, 0).text() in self.columnArray:
                    QtWidgets.QMessageBox.information(self, '警告', 'ID不能重复')
                    tableWidgetName.blockSignals(True)
                    tableWidgetName.setItem(row, 0, QtWidgets.QTableWidgetItem(self.selectedValue))
                    tableWidgetName.blockSignals(False)
                    return
                if tableWidgetName.item(row,0).text() not in changeRow and tableWidgetName.item(row, 0).text() not in self.columnArray:
                    if self.selectedValue == '':
                        return
                    else:
                        self.selectedValue = ''
                        changeRow.append(self.selectedValue)
                        addRow.append([tableWidgetName.item(row, 0).text(), tableWidgetName.item(row, 1).text()])
                        return

        if rowFilled:
            try:
                result = [tableWidgetName.item(row, 0).text(), tableWidgetName.item(row, 1).text()]
                for test in addRow:
                    if test[0] == result[0]:
                        addRow = [x for x in addRow if result[0] not in x]
                        break
                addRow.append(result)
                rowCount = tableWidgetName.rowCount()
            except Exception as e:
                print(e)

    def saveProductRowSlot(self):
        self.__saveRow('prod', self.delProdRow, self.changeProdRow, self.addProdRow, self.productShowTable)

    def saveMaterialRowSlot(self):
        self.__saveRow('mat', self.delMatRow, self.changeMatRow, self.addMatRow, self.materialShowTable)

    def __saveRow(self, type, delRow, changeRow, addRow, tableWidgetName):
        # data = []
        # for row in range(tableWidgetName.rowCount()):
        #     data.append(tableWidgetName.item(row, 0).text())
        #     if len(set(data)) < len(data):
        #         QtWidgets.QMessageBox.information(self, '警告', 'ID有重复项，请检查')
        #         return
        #     else:
                
        while len(delRow) > 0:
            self.sql.deleteProdMatRow(type, delRow.pop())
        while len(changeRow) > 0:
            self.sql.deleteProdMatRow(type, changeRow.pop())
        while len(addRow) > 0:
            try:
                self.sql.addProdMatRow(type, addRow.pop())
            except Exception as e:
                if e.args[0] == 1062:
                    QtWidgets.QMessageBox.information(self, '警告', 'ID不能重复')
                    deleteRow = tableWidgetName.rowCount() - 1
                    tableWidgetName.removeRow(deleteRow)
                    if type == 'prod':
                        self.prodRowCount = tableWidgetName.rowCount()
                    elif type == 'mat':
                        self.matRowCount = tableWidgetName.rowCount()
                else:
                    print(e)
        QtWidgets.QMessageBox.information(self, '提示', '保存成功')

    def selectedValueSave(self, tableWidgetName):
        if len(tableWidgetName.selectedItems()) != 0:
            self.selectedValue = tableWidgetName.selectedItems()[0].text()
            self.columnArray = []
            for row in range(tableWidgetName.rowCount() - 1):
                item = tableWidgetName.item(row, 0)
                if item:
                    self.columnArray.append(item.text())
        else:
            self.selectedValue = ''
            self.columnArray = []
            for row in range(tableWidgetName.rowCount() - 1):
                item = tableWidgetName.item(row, 0)
                if item:
                    self.columnArray.append(item.text())

    def addMatToProdSlot(self):
        if self.selectRowItemText != '':
            self.addMatToProdWindow = AddMaterialWindow(self.selectRowItemText, self.sql)
            self.addMatToProdWindow.show()
        else:
            QtWidgets.QMessageBox.information(self, '提示', '请先选择一行数据')
        
    def selectRowSlot(self, item):
        row = item.row()
        self.selectRowItemText = self.productShowTable.item(row, 1).text()
