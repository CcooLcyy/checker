from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QImage, QPixmap
import sys, os, cv2, time
sys.path.append('src')
from func.data import Data

class VoidWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(VoidWindow, self).__init__()
        uic.loadUi('src/ui/voidWindow.ui', self)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # 添加页面区
        self.mainWindow = uic.loadUi('src/ui/mainWindow.ui')
        self.dataWindow = uic.loadUi('src/ui/dataWindow.ui')
        self.dataMarkWindow = uic.loadUi('src/ui/dataMarkWindow.ui')

        self.stackedWidget.addWidget(self.mainWindow)
        self.stackedWidget.addWidget(self.dataWindow)
        self.stackedWidget.addWidget(self.dataMarkWindow)

        # 跳转页面信号区
        self.mainWindow.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.dataWindow.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.dataWindow.toDataMarkWindowButton.clicked.connect(self.toDataMarkWindowSlot)
        self.dataMarkWindow.toDataWindowButton.clicked.connect(self.toDataWindowSlot)

        # mainWindow信号区

        # dataWindow信号区
        self.dataWindow.data = Data()

        self.dataWindow.clearDataMarkOutputShow.clicked.connect(self.clearDataMarkOutputShowSlot)
        self.dataWindow.clearDatasetCollectOutputShow.clicked.connect(self.clearDatasetCollectOutputShowSlot)
        self.dataWindow.loadMarkedImageByDir.clicked.connect(self.loadMarkedImageByDirSlot)
        self.dataWindow.saveMarkedDataset.clicked.connect(self.saveMarkedDatasetSlot)
        self.dataWindow.loadUnMarkedDataByDir.clicked.connect(self.loadUnMarkedDataByDirSlot)

        # dataMarkWindow信号区
        self.dataMarkWindow.imagePath = []
        self.dataMarkWindow.imageCount = 0

        self.dataMarkWindow.startShowUnmarkedImage.clicked.connect(self.saveImagePathInArraySlot)

    # 跳转页面槽函数
    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(1)

    def toMainWindowSlot(self):
        self.stackedWidget.setCurrentIndex(0)

    def toDataMarkWindowSlot(self):
        self.stackedWidget.setCurrentIndex(2)

    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(1)

    # mainWindow槽函数

    # dataWindow槽函数
    def clearDataMarkOutputShowSlot(self):
        self.dataWindow.dataMarkOutputShow.clear()
    
    def clearDatasetCollectOutputShowSlot(self):
        self.dataWindow.datasetCollectOutputShow.clear()
    
    def loadMarkedImageByDirSlot(self):
        path = self.dataWindow.data.loadMarkedImageByDir()
        if path != '':
            self.dataWindow.datasetCollectOutputShow.appendPlainText('已选取文件夹：' + path)
        else:
            self.dataWindow.datasetCollectOutputShow.appendPlainText('未选取目录')
   
    def saveMarkedDatasetSlot(self):
        if self.dataWindow.data.image == None and self.dataWindow.data.label == None:
            self.dataWindow.datasetCollectOutputShow.appendPlainText('请先选择载入打标数据方式')
        else:
            path = self.dataWindow.data.saveMarkedDataset()
            self.dataWindow.datasetCollectOutputShow.appendPlainText('文件保存完成：' + path)
   
    def loadUnMarkedDataByDirSlot(self):
        self.dataMarkWindow.path = self.dataWindow.data.loadUnMarkedDataByDir()
        if self.dataMarkWindow.path == '':
            self.dataWindow.dataMarkOutputShow.appendPlainText('未选取目录')
        else:
            self.dataWindow.dataMarkOutputShow.appendPlainText('目录位置' + self.dataMarkWindow.path)
    
    # dataMarkWindow槽函数
    def saveImagePathInArraySlot(self):
        self.dataMarkWindow.path = self.dataMarkWindow.path
        if self.dataMarkWindow.path == '':
            pass
        else:
            for fileName in os.listdir(self.dataMarkWindow.path):
                if fileName != 'Thumbs.db':
                # 避免将系统缩略图文件导入其中
                    self.dataMarkWindow.imagePath.append(self.dataMarkWindow.path + '/' + fileName)
                    if len(self.dataMarkWindow.imagePath) == 1:
                        image = self.dataWindow.data.getImageData(fileName, self.dataMarkWindow.path)
                        height, width, channel = image.shape
                        bytesPerLine = 3 * width
                        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                        self.dataMarkWindow.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = VoidWindow()
    mainWin.show()
    sys.exit(app.exec_())