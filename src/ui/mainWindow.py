from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from ui.ui_mainWindow import Ui_mainWindow
from ui.changeLocalUserPassword import ChangeLocalUserPassword

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    toLoginWindowSignal = QtCore.pyqtSignal()
    def __init__(self, userName):
        super().__init__()
        self.setupUi(self)

        self.userName = userName
        
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.changeUserButton.clicked.connect(self.toLoginWindowSlot)
        self.changeUserPasswordButton.clicked.connect(self.changeUserPasswordSlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()
    
    def toLoginWindowSlot(self):
        self.toLoginWindowSignal.emit()
    
    def changeUserPasswordSlot(self):
        self.changeLocalUserPassword = ChangeLocalUserPassword(self.userName)
        self.changeLocalUserPassword.show()