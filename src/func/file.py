import tkinter as tk
from tkinter import filedialog

class File():
    def __init__(self):
        pass

    def selectDirPath(self):
        root = tk.Tk()
        root.withdraw()
        folderPath = filedialog.askdirectory()
        
        return folderPath

if __name__ == '__main__':
    pass