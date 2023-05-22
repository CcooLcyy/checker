import sys
sys.path.append('src')
from PyQt5 import QtWidgets, QtCore
from ui.ui_addMaterialWindow import Ui_addMaterialWindow
from func.mysql import Mysql

class AddMaterialWindow(QtWidgets.QWidget, Ui_addMaterialWindow):
    def __init__(self, prodName):
        super().__init__()
        self.setupUi(self)

        self.prodAddMatTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.prodAddMatTable.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.sql = Mysql()
        self.prodName = prodName
        self.matList = []
        self.prodId = self.sql.queryProdIdByProdName(self.prodName)
        self.__initMatRow()
        self.showMaterialLabel.setText(prodName)

        self.addToBomButton.clicked.connect(self.addToBomSlot)
        self.prodAddMatTable.itemSelectionChanged.connect(self.changeMatList)

    def __initMatRow(self):
        result = self.sql.queryAllMaterial()
        self.prodAddMatTable.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.prodAddMatTable.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.prodAddMatTable.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            itemRow += 1
        result = self.sql.queryBomByProdId(self.prodId)
        self.matList = [item for sub in result for item in sub]
        for matId in self.matList:
            for row in range(self.prodAddMatTable.rowCount()):
                item = self.prodAddMatTable.item(row, 0)
                if item.text() == str(matId):
                    self.prodAddMatTable.setCurrentCell(row, 0, QtCore.QItemSelectionModel.Select)
                    self.prodAddMatTable.setCurrentCell(row, 1, QtCore.QItemSelectionModel.Select)
        print(self.matList)

    def addToBomSlot(self):
        prodIdInTuple = self.sql.queryProdIdByProdName(self.prodName)
        prodId = prodIdInTuple[0][0]
        self.sql.deleteBomByProdId(prodId)
        for matId in self.matList:
            matList = [str(prodId), str(matId)]
            self.sql.addToBom(matList)
        self.close()
        
    def changeMatList(self):
        self.matList = []
        selectedItems = self.prodAddMatTable.selectedItems()
        for item in selectedItems:
            if item.column() == 0:
                content = item.text()
                self.matList.append(int(content))