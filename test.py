from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QImage, QPixmap
import sys, os, cv2, time
sys.path.append('src')
from func.data import Data
from ui.ui_voidWindow import Ui_voidWindow
from ui.ui_mainWindow import Ui_mainWindow
from ui.ui_dataWindow import Ui_dataPageWindow
from ui.ui_dataMarkWindow import Ui_dataMarkWindow

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    mySignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)

    def toDataWindowSlot(self):
        self.mySignal.emit()

class VoidWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/ui/voidWindow.ui', self)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.mainWindow = MainWindow()

        self.stackedWidget.addWidget(self.mainWindow)

        self.mainWindow.mySignal.connect(self.toDataWindowSlot)

    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = VoidWindow()
    mainWin.show()
    sys.exit(app.exec_())