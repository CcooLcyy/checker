import os, sys
sys.path.append('src')
from func.file import File
from func.mysql import Mysql
import numpy as np
import cv2
from PyQt5.QtGui import QImage
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

class Data():
    def __init__(self):
        self.file = File()
        self.image = None
        self.label = None
        self.sql = Mysql()

    def getImageDataFromPath(self, folderPath):
        try:
            imageArr = []
            for fileName in folderPath:
                if fileName != 'Thumbs.db':
                # 避免将系统缩略图文件导入其中
                    image = plt.imread(fileName)
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    imageArr.append(image)
            return imageArr
        except Exception as e:
            print(e)


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
                    image = plt.imread(filePath)
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    
                    label = self.sql.queryMarkByName(fileName.split('.')[0])
                    if len(label) == 0:
                        label = 'pass'
                    else:
                        if label[0][0] == 1:
                            label = 'A'
                        elif label[0][1] == 1:
                            label = 'B'
                        elif label[0][2] == 1:
                            label = 'C'

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

        return qImg, image
    
    def handleTrainingData(self, path):
        data = np.load(path)
        image, label = data['image'], data['label']
        indices = np.arange(image.shape[0])
        np.random.shuffle(indices)
        image, label = image[indices], label[indices]

        encoder = LabelEncoder()
        label = encoder.fit_transform(label)
        label = to_categorical(label)

        return image, label

if __name__ == '__main__':
    test = Data()
    test.loadMarkedImageByDir()
    test.saveMarkedDataset()