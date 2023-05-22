from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from func.mysql import Mysql
from ui.ui_selectMat import Ui_selecetMat

class SelectMat(QtWidgets.QWidget, Ui_selecetMat):
    selectValue = QtCore.pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sql = Mysql()
        self.name = ''
        self.matTableShow.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.__initMatShow()

        self.selectMatButton.clicked.connect(self.selectProdSlot)
        self.matTableShow.itemClicked.connect(self.selectItem)

    def __initMatShow(self):
        result = self.sql.queryAllMaterial()
        self.matTableShow.setRowCount(len(result))
        itemRow = 0
        for row, column in result:
            self.matTableShow.setItem(itemRow, 0, QtWidgets.QTableWidgetItem(str(row)))
            self.matTableShow.setItem(itemRow, 1, QtWidgets.QTableWidgetItem(column))
            itemRow += 1

    def selectProdSlot(self):
        self.selectValue.emit(self.id, self.name)
        self.close()

    def selectItem(self, item):
        row = item.row()
        result = self.matTableShow.item(row, 1).text()
        self.name = result
        self.id = self.matTableShow.item(row, 0).text()