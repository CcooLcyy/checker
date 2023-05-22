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
        self.__initUserNameComboBox()
        self.__initProdNameComboBox()
        self.__initMatNameComboBox()
        self.__initMarkTimeComboBox()
        self.__initClassComboBox()

    def __initUserNameComboBox(self):
        allUser = [item for subtuple in self.sql.queryAllUser() for item in subtuple]
        allUser.remove('admin')
        self.userNameComboBox.addItems(allUser)

    def __initProdNameComboBox(self):
        self.allProd = [_ for subtuple in self.sql.queryAllProduct() for _ in subtuple]
        self.allProd = [_ for _ in self.allProd if not isinstance(_, int)]
        self.prodNameComboBox.addItems(self.allProd)
    
    def __initMatNameComboBox(self):
        self.allMat = [_ for subtuple in self.sql.queryAllMaterial() for _ in subtuple]
        self.allMat = [_ for _ in self.allMat if not isinstance(_, int)]
        self.matNameComboBox.addItems(self.allMat)

    def __initMarkTimeComboBox(self):   
        self.allTime = [_.date().strftime('%Y-%m-%d') for subtuple in self.sql.queryAllTime() for _ in subtuple]
        self.allTime = set(self.allTime)
        self.markTimeComboBox.addItems(self.allTime)

    def __initClassComboBox(self):
        aMark = set([_ for subtuple in self.sql.queryAMarks() for _ in subtuple])
        bMark = set([_ for subtuple in self.sql.queryBMarks() for _ in subtuple])
        cMark = set([_ for subtuple in self.sql.queryCMarks() for _ in subtuple])
        if 1 in aMark:
            self.classComboBox.addItem('A')
        if 1 in bMark:
            self.classComboBox.addItem('B')
        if 1 in cMark:
            self.classComboBox.addItem('C')


    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

    def toProdMatManageWindowSlot(self):
        self.toProdMatManageWindowSignal.emit()