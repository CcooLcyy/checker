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
    
    def renameData(self, filePath, savePath, mark):
        root, ext = os.path.splitext(filePath)
        savedFileName = f'{savePath}/{mark}_1{ext}'
        if not os.path.exists(savedFileName):
            os.rename(filePath, savedFileName)
        else:
            i = 2
            while True:
                savedFileName = f'{savePath}/{mark}_{i}{ext}'
                if not os.path.exists(savedFileName):
                    os.rename(filePath, savedFileName)
                    break
                i += 1

if __name__ == '__main__':
    pass