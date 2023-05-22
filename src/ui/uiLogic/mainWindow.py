from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from ui.ui_mainWindow import Ui_mainWindow
from ui.uiLogic.changeLocalUserPassword import ChangeLocalUserPassword

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    toLoginWindowSignal = QtCore.pyqtSignal()
    toProductManageWindowSignal = QtCore.pyqtSignal()
    toStateWindowSingal = QtCore.pyqtSignal()
    def __init__(self, userName):
        super().__init__()
        self.setupUi(self)

        self.userName = userName
        
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.toProductManageWindowButton.clicked.connect(self.toProductManageWindowSlot)
        self.toStateWindowButton.clicked.connect(self.toStateWindowSlot)
        self.changeUserButton.clicked.connect(self.toLoginWindowSlot)
        self.changeUserPasswordButton.clicked.connect(self.changeUserPasswordSlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()
    
    def toLoginWindowSlot(self):
        self.toLoginWindowSignal.emit()

    def toProductManageWindowSlot(self):
        self.toProductManageWindowSignal.emit()
    
    def toStateWindowSlot(self):
        self.toStateWindowSingal.emit()
    
    def toStateWindowSlot(self):
        self.toStateWindowSingal.emit()
    
    def changeUserPasswordSlot(self):
        self.changeLocalUserPassword = ChangeLocalUserPassword(self.userName)
        self.changeLocalUserPassword.show()