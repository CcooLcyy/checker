from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from ui.ui_mainWindow import Ui_mainWindow

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    toLoginWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.changeUserButton.clicked.connect(self.toLoginWindowSlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()
    
    def toLoginWindowSlot(self):
        self.toLoginWindowSignal.emit()