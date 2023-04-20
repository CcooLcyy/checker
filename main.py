import sys
sys.path.append('src')
from PyQt5 import QtWidgets, uic
from func.data import Data

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('src/ui/mainWindow.ui', self)

        self.toDataWindowButton.clicked.connect(self.toDataWindow)
        
    def toDataWindow(self):
        self.hide()
        self.dataWindow = DataWindow()
        self.dataWindow.show()

class DataWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(DataWindow, self).__init__()
        uic.loadUi('src/ui/dataWindow.ui', self)

        self.data = Data()

        self.toMainWindowButton.clicked.connect(self.toMainWindow)
        self.loadMarkedImageByDir.clicked.connect(self.loadMarkedImageByDirSlot)
        self.saveMarkedDataset.clicked.connect(self.saveMarkedDatasetSlot)

    def toMainWindow(self):
        self.hide()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def loadMarkedImageByDirSlot(self):
        path = self.data.loadMarkedImageByDir()
        if path != '':
            self.outputShow.appendPlainText('已选取文件夹：' + path)
        else:
            self.outputShow.appendPlainText('未选取目录')

    def saveMarkedDatasetSlot(self):
        if self.data.image == None:
            self.outputShow.appendPlainText('请先选择载入打标数据方式')
        else:
            path = self.data.saveMarkedDataset()
            self.outputShow.appendPlainText('文件保存完成：' + path)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())