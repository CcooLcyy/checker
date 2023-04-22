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
    toDataWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()

class DataWindow(QtWidgets.QWidget, Ui_dataPageWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toDataMarkWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = Data()
        
        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toDataMarkWindowButton.clicked.connect(self.toDataMarkWindowSlot)
        self.loadMarkedImageByDir.clicked.connect(self.loadMarkedImageByDirSlot)
        self.clearDataMarkOutputShow.clicked.connect(self.clearDataMarkOutputShowSlot)
        self.clearDatasetCollectOutputShow.clicked.connect(self.clearDatasetCollectOutputShowSlot)
        self.saveMarkedDataset.clicked.connect(self.saveMarkedDatasetSlot)
        self.loadUnMarkedDataByDir.clicked.connect(self.loadUnMarkedDataByDirSlot)

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()
    
    def toDataMarkWindowSlot(self):
        self.toDataMarkWindowSignal.emit()

    def loadMarkedImageByDirSlot(self):
        path = self.data.loadMarkedImageByDir()
        if path != '':
            self.datasetCollectOutputShow.appendPlainText('已选取文件夹：' + path)
        else:
            self.datasetCollectOutputShow.appendPlainText('未选取目录')
    
    def clearDataMarkOutputShowSlot(self):
        self.dataMarkOutputShow.clear()
    
    def clearDatasetCollectOutputShowSlot(self):
        self.datasetCollectOutputShow.clear()
   
    def saveMarkedDatasetSlot(self):
        if self.data.image == None and self.data.label == None:
            self.datasetCollectOutputShow.appendPlainText('请先选择载入打标数据方式')
        else:
            path = self.data.saveMarkedDataset()
            if path != None:
                self.datasetCollectOutputShow.appendPlainText('文件保存完成：' + path)

    def loadUnMarkedDataByDirSlot(self):
        self.loadImagePath = self.data.loadUnMarkedDataByDir()
        if self.loadImagePath == '':
            self.dataMarkOutputShow.appendPlainText('未选取目录')
        else:
            self.dataMarkOutputShow.appendPlainText('目录位置' + self.loadImagePath)

class DataMarkWindow(QtWidgets.QWidget, Ui_dataMarkWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = Data()
        self.imagePath = []
        self.imageCount = 0
        self.loadImagePath = ''
        self.savePath = ''

        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
    #     self.startShowUnmarkedImageButton.clicked.connect(self.saveImagePathInArraySlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()
    # def saveImagePathInArraySlot(self):
    #     self.dataMarkWindow.savePath = self.dataMarkWindow.data.file.selectDirPath()
    #     self.dataMarkWindow.loadImagePath = self.dataMarkWindow.loadImagePath
    #     if self.dataMarkWindow.loadImagePath == '':
    #         pass
    #     else:
    #         for fileName in os.listdir(self.dataMarkWindow.loadImagePath):
    #             if fileName != 'Thumbs.db':
    #             # 避免将系统缩略图文件导入其中
    #                 self.dataMarkWindow.imagePath.append(self.dataMarkWindow.loadImagePath + '/' + fileName)
    #                 if len(self.dataMarkWindow.imagePath) == 1:
    #                     image = self.dataWindow.data.getImageData(fileName, self.dataMarkWindow.loadImagePath)
    #                     height, width, channel = image.shape
    #                     bytesPerLine = 3 * width
    #                     qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    #                     self.dataMarkWindow.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))

class VoidWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/ui/voidWindow.ui', self)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.mainWindow = MainWindow()
        self.dataWindow = DataWindow()
        self.dataMarkWindow = DataMarkWindow()

        self.stackedWidget.addWidget(self.mainWindow)
        self.stackedWidget.addWidget(self.dataWindow)
        self.stackedWidget.addWidget(self.dataMarkWindow)

        self.mainWindow.toDataWindowSignal.connect(self.toDataWindowSlot)
        self.dataWindow.toMainWindowSignal.connect(self.toMainWindowSlot)
        self.dataWindow.toDataMarkWindowSignal.connect(self.toDataMarkWindowSlot)
        self.dataMarkWindow.toDataWindowSignal.connect(self.toDataWindowSlot)

    def toMainWindowSlot(self):
        self.stackedWidget.setCurrentIndex(0)

    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(1)

    def toDataMarkWindowSlot(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = VoidWindow()
    mainWin.show()
    sys.exit(app.exec_())