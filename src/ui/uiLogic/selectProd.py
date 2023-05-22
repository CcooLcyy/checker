from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from func.mysql import Mysql
from ui.ui_selectProd import Ui_selectProd

class SelectProd(QtWidgets.QWidget, Ui_selectProd):
    selectValue = QtCore.pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sql = Mysql()
        self.name = ''
        self.prodTableShow.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.__initProdShow()

        self.selectProdButton.clicked.connect(self.selectProdSlot)
        self.prodTableShow.itemClicked.connect(self.selectItem)

    def __initProdShow(self):
        result = self.sql.queryAllProduct()
        self.prodTableShow.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.prodTableShow.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.prodTableShow.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            itemRow += 1

    def selectProdSlot(self):
        self.selectValue.emit(self.id, self.name)
        self.close()

    def selectItem(self, item):
        row = item.row()
        result = self.prodTableShow.item(row, 1).text()
        self.name = result
        self.id = self.prodTableShow.item(row, 0).text()