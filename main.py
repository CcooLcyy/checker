import sys
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('src/ui/mainWindow.ui', self)

        self.toDataWindowButton.clicked.connect(self.toDataWindow)
        # self.showing.appendPlainText()
        
    def toDataWindow(self):
        self.hide()
        self.dataWindow = DataWindow()
        self.dataWindow.show()

class DataWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DataWindow, self).__init__()
        uic.loadUi('src/ui/dataWindow.ui', self)

        self.toMainWindowButton.clicked.connect(self.toMainWindow)

    def toMainWindow(self):
        self.hide()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())