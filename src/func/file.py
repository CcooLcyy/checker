import tkinter as tk
from tkinter import filedialog
import os

class File():
    def __init__(self):
        pass

    def selectDirPath(self):
        root = tk.Tk()
        root.withdraw()
        folderPath = filedialog.askdirectory()
        
        return folderPath
    
    def selectFilePath(self):
        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()

        return filePath
    
    def renameData(self, filePath, savePath, matName):
        root, ext = os.path.splitext(filePath)
        mat = root.split('/')[-1].split('_')[0]
        savedFileName = f'{savePath}/{matName}/{mat}_1{ext}'
        if not os.path.exists(savedFileName):
            if not os.path.exists(f'{savePath}/{matName}'):
                os.makedirs(f'{savePath}/{matName}')
            os.rename(filePath, savedFileName)
            className = mat + '_' + '1'
            return className
        else:
            i = 2
            while True:
                savedFileName = f'{savePath}/{matName}/{mat}_{i}{ext}'
                if not os.path.exists(savedFileName):
                    os.rename(filePath, savedFileName)
                    break
                i += 1
            className = mat + '_' + str(i)
            return className

if __name__ == '__main__':
    pass