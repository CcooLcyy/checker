from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from func.mysql import Mysql
from ui.ui_stateWindow import Ui_stateWindow
import datetime

class StateWindow(QtWidgets.QWidget, Ui_stateWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toDataWindowSignal = QtCore.pyqtSignal()
    toProdMatManageWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sql = Mysql()

        self.__initComboBox()

        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.toProdMatManageWindowButton.clicked.connect(self.toProdMatManageWindowSlot)

    def __initComboBox(self):
        self.allUser = [item for subtuple in self.sql.queryAllUser() for item in subtuple]
        self.allUser.remove('admin')
        self.userNameComboBox.addItems(self.allUser)

        self.allProd = [_ for subtuple in self.sql.queryAllProduct() for _ in subtuple]
        self.allProd = [_ for _ in self.allProd if not isinstance(_, int)]
        self.prodNameComboBox.addItems(self.allProd)

        self.allMat = [_ for subtuple in self.sql.queryAllMaterial() for _ in subtuple]
        self.allMat = [_ for _ in self.allMat if not isinstance(_, int)]
        self.matNameComboBox.addItems(self.allMat)

        self.allTime = [_.date().strftime('%Y-%m-%d') for subtuple in self.sql.queryAllTime() for _ in subtuple]
        self.allTime = set(self.allTime)
        self.markTimeComboBox.addItems(self.allTime)

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

    def toProdMatManageWindowSlot(self):
        self.toProdMatManageWindowSignal.emit()


    

    # (
        # (datetime.datetime(2023, 5, 21, 21, 25, 16),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 7),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 8),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 8),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 8),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 9),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 9),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 9),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 9),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 9),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 10),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 10),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 10),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 10),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 11),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 11),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 11),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 5),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 11),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 11),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 12),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 12),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 12),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 12),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 12),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 5),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 6),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 6),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 6),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 6),), 
    #     (datetime.datetime(2023, 5, 22, 10, 4, 7),)
    # )


# [
#     datetime.datetime(2023, 5, 21, 21, 25, 16), 
#     datetime.datetime(2023, 5, 22, 10, 4, 7), 
#     datetime.datetime(2023, 5, 22, 10, 4, 8), 
#     datetime.datetime(2023, 5, 22, 10, 4, 8), 
#     datetime.datetime(2023, 5, 22, 10, 4, 8), 
#     datetime.datetime(2023, 5, 22, 10, 4, 9), 
#     datetime.datetime(2023, 5, 22, 10, 4, 9), 
#     datetime.datetime(2023, 5, 22, 10, 4, 9), 
# ]