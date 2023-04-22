import os, sys
sys.path.append('src')
from func.file import File
import numpy as np
import cv2
from PyQt5.QtGui import QImage, QPixmap

class Data():
    def __init__(self):
        self.file = File()
        self.image = None
        self.label = None

    def loadMarkedImageByDir(self):
        sumImage = []
        sumLabel = []
        folderPath = self.file.selectDirPath()
        if folderPath == '':
            pass
        else:
            for fileName in os.listdir(folderPath):
                if fileName != 'Thumbs.db':
                # 避免将系统缩略图文件导入其中
                    filePath = os.path.join(folderPath, fileName)
                    image = cv2.imread(filePath)
                    label = np.array(os.path.splitext(fileName)[0].split('_')[0], dtype='str')
                    sumImage.append(image)
                    sumLabel.append(label)
            self.image, self.label = sumImage, sumLabel
        return folderPath

    def saveMarkedDataset(self):
        saveDirPath = self.file.selectDirPath()
        if saveDirPath == '':
            pass
        else:
            savePath = saveDirPath + '/datasets.npz'
            np.savez(savePath, image = self.image, label = self.label)
            self.image = None
            self.label = None
            return savePath
    
    def loadUnMarkedDataByDir(self):
        filePath = self.file.selectDirPath()
        return filePath

    def imageShow(self, filePath):
        image = cv2.imread(filePath)
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        return qImg


if __name__ == '__main__':
    test = Data()
    test.loadMarkedImageByDir()
    test.saveMarkedDataset()