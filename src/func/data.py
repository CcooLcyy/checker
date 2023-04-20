import os, sys, time
sys.path.append('src')
from func.file import File
import numpy as np
import cv2

class Data():
    def __init__(self):
        self.file = File()
        self.image = None
        self.label = None

    def loadMarkedImageByDir(self):
        sumImage = []
        sumLabel = []
        folderPath = self.file.selectDirPath()
        for fileName in os.listdir(folderPath):
            if fileName != 'Thumbs.db':
            # 避免将系统缩略图文件导入其中
                filePath = os.path.join(folderPath, fileName)
                image = cv2.imread(filePath)
                label = np.array(os.path.splitext(fileName)[0].split('_')[0], dtype='str')
                sumImage.append(image)
                sumLabel.append(label)
        self.image, self.label = sumImage, sumLabel

    def saveMarkedDataset(self):
        saveDirPath = self.file.selectDirPath()
        savePath = saveDirPath + '/datasets.npz'
        np.savez(savePath, image = self.image, label = self.label)
    
    def loadUnMarkedDataByDir(self):
        '''
        未完成
        '''
        filePath = self.file.selectDirPath()

    def saveMarkedImage(self):
        filePath = self.file.selectDirPath()

if __name__ == '__main__':
    test = Data()
    test.loadMarkedImageByDir()
    test.saveMarkedDataset()