import os, sys
sys.path.append('src')
from func.file import File
import numpy as np
import cv2

class LoadData():
    def __init__(self):
        self.file = File()
        self.folderPath = self.file.selectDir()

    def __loadDataByDir(self):
        sumImage = []
        sumLabel = []
        for fileName in os.listdir(self.folderPath):
            if fileName != 'Thumbs.db':
            # 避免将系统缩略图文件导入其中
                filePath = os.path.join(self.folderPath, fileName)
                image = cv2.imread(filePath)
                label = np.array(os.path.splitext(fileName)[0].split('_')[0], dtype='str')
                sumImage.append(image)
                sumLabel.append(label)
        return sumImage, sumLabel

    def saveData(self):
        image, label = self.__loadDataByDir()
        np.savez('data.npz', image = image, label = label)

if __name__ == '__main__':
    test = LoadData()
    test.saveData()