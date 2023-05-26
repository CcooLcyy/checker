from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from ui.ui_stateWindow import Ui_stateWindow
import datetime

class StateWindow(QtWidgets.QWidget, Ui_stateWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toDataWindowSignal = QtCore.pyqtSignal()
    toProdMatManageWindowSignal = QtCore.pyqtSignal()
    def __init__(self, sql):
        super().__init__()
        self.setupUi(self)

        self.sql = sql

        self.__initComboBox()
        self.infoTableShow.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.infoTableShow.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.toProdMatManageWindowButton.clicked.connect(self.toProdMatManageWindowSlot)
        self.queryButton.clicked.connect(self.querySlot)

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

    def querySlot(self):
        userName, prodId, matId, markTime, markClass = self.__getCurrentText()
        prodId = self.__queryProdIdByName()
        matId = self.__queryMatIdByName()
        if userName == '（用户名）' or prodId == '（产品名称）' or matId == '（物料名称）' or markTime == '（打标时间）' or markClass == '（类别）':
            self.infoTableShow.setRowCount(0)
            return
        if markClass == 'A':
            a, b, c = '1', '0', '0'
        elif markClass == 'B':
            a, b, c = '0', '1', '0'
        elif markClass == 'C':
            a, b, c = '0', '0', '1'
        elif markClass == '*':
            a, b, c = '*', '*', '*'

        queryResult = self.sql.queryMarkByConditions(userName, prodId, matId, markTime, a, b, c)
        self.__addItemToTableWidget(queryResult)

    def __turnToClass(self, queryResult):
        if queryResult:
            firstList = list(queryResult[:-3])
            lastList = list(queryResult[-3:])
            result = lastList.index(1)
            if result == 0:
                firstList.append('A')
            elif result == 1:
                firstList.append('B')
            elif result == 2:
                firstList.append('C')

            return firstList

    def __getCurrentText(self):
        userName = self.userNameComboBox.currentText()
        prodName = self.prodNameComboBox.currentText()
        matName = self.matNameComboBox.currentText()
        markTime = self.markTimeComboBox.currentText()
        markClass = self.classComboBox.currentText()
        return userName, prodName, matName, markTime, markClass
    
    def __queryProdIdByName(self):
        userName, prodName, matName, markTime, markClass = self.__getCurrentText()
        if prodName == '*':
            prodId = prodName
        else:
            prodId = [_ for subtuple in self.sql.queryProdIdByProdName(prodName) for _ in subtuple]
            if len(prodId) != 0:
                prodId = prodId[0]
        return prodId
    
    def __queryMatIdByName(self):
        userName, prodName, matName, markTime, markClass = self.__getCurrentText()
        if matName == '*':
            matId = matName
        else:
            matId = [_ for subtuple in self.sql.queryMatIdByName(matName) for _ in subtuple]
            if len(matId) != 0:
                matId = matId[0]
        return matId

    def __addItemToTableWidget(self, queryResult):
        self.infoTableShow.setRowCount(0)
        for oneRow in queryResult:
            oneRow = self.__turnToClass(oneRow)
            row = self.infoTableShow.rowCount()
            self.infoTableShow.insertRow(row)
            for index, value in enumerate(oneRow):
                if type(value) == datetime.datetime:
                    value = value.strftime('%Y-%m-%d %H:%M:%S')
                self.infoTableShow.setItem(row, index, QtWidgets.QTableWidgetItem(value))

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

    def toProdMatManageWindowSlot(self):
        self.toProdMatManageWindowSignal.emit()
