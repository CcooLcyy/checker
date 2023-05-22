from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
import sys, os
sys.path.append('src')
from func.data import Data
from func.file import File
from func.mysql import Mysql
from ui.uiLogic.selectProd import SelectProd
from ui.uiLogic.selectMat import SelectMat
from ui.ui_dataWindow import Ui_dataPageWindow

class DataWindow(QtWidgets.QWidget, Ui_dataPageWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    toProductManageWindowSignal = QtCore.pyqtSignal()
    toStateWindowSingal = QtCore.pyqtSignal()
    def __init__(self, userName, sql):
        super().__init__()
        self.setupUi(self)
        self.data = Data()
        self.file = File()
        self.sql = sql
        self.imagePath = []
        self.imageCount = 0
        self.loadImagePath = ''
        self.savePath = ''
        self.prodId = None
        self.prodName = None
        self.matId = None
        self.matName = None
        self.userName = userName
        
        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.toProductManageWindowButton.clicked.connect(self.toProductManageWindowSlot)
        self.toStateWindowButton.clicked.connect(self.toStateWindowSingal)
        self.clearDataMarkOutputShowButton.clicked.connect(self.clearDataMarkOutputShowSlot)
        self.saveMarkedDataset.clicked.connect(self.saveMarkedDatasetSlot)
        self.loadUnMarkedDataByDir.clicked.connect(self.loadUnMarkedDataByDirSlot)
        self.startShowUnmarkedImageButton.clicked.connect(self.startShowUnmarkedImageSlot)
        self.qualifiedProductButton.clicked.connect(self.qualifiedProductSlot)
        self.AClassButton.clicked.connect(self.AClassSlot)
        self.BClassButton.clicked.connect(self.BClassSlot)
        self.CClassButton.clicked.connect(self.CClassSlot)
        self.choiceProdByIdButton.clicked.connect(self.choiceProdByIdSlot)
        self.choiceMatByIdButton.clicked.connect(self.choiceMatByIdSlot)

    def choiceProdByIdSlot(self):
        self.choiceProdById = SelectProd()
        self.choiceProdById.selectValue.connect(self.choiceProdByIdSignal)
        self.choiceProdById.show()
    
    def choiceProdByIdSignal(self, id, name):
        self.prodId = id
        self.prodName = name
        print(self.prodId)

    def choiceMatByIdSlot(self):
        self.choiceMatById = SelectMat()
        self.choiceMatById.selectValue.connect(self.choiceMatByIdSignal)
        self.choiceMatById.show()

    def choiceMatByIdSignal(self, id, name):
        self.matId = id
        self.matName = name
        print(self.matId)

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

    def toProductManageWindowSlot(self):
        self.toProductManageWindowSignal.emit()

    def toStateWindowSlot(self):
        self.toStateWindowSingal.emit()

    def __divideRanksShow(self, mark):
        if len(self.imagePath) == 0:
            self.dataMarkOutputShow.appendPlainText('请先点击开始打标')
        else:
            if self.imageCount >= len(self.imagePath):
                self.dataMarkOutputShow.appendPlainText('图片打标已完成，请重新选择数据')
            else:
                filePath = self.imagePath[self.imageCount]
                classId = self.file.renameData(filePath, self.savePath, self.matName)
                if mark == 'A':
                    aClass = True
                    bClass = False
                    cClass = False
                elif mark == 'B':
                    aClass = False
                    bClass = True
                    cClass = False
                elif mark == 'C':
                    aClass = False
                    bClass = False
                    cClass = True
                elif mark == 'pass':
                    aClass = False
                    bClass = False
                    cClass = False
                    # if self.imageCount >= len(self.imagePath):
                    #     self.dataMarkOutputShow.appendPlainText('图片打标完成')
                    #     self.UnmarkedImageShow.clear()
                    # else:
                    #     qImg = self.data.imageShow(self.imagePath[self.imageCount])
                    #     self.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))

                if mark == 'pass':
                    pass
                else:
                    self.sql.insertMarkData(classId, self.matId, self.prodId, self.userName, aClass, bClass, cClass)

                self.imageCount += 1
                if self.imageCount >= len(self.imagePath):
                    self.dataMarkOutputShow.appendPlainText('图片打标完成')
                    self.UnmarkedImageShow.clear()
                else:
                    qImg = self.data.imageShow(self.imagePath[self.imageCount])
                    self.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))

    def CClassSlot(self):
        self.__divideRanksShow('C')

    def BClassSlot(self):
        self.__divideRanksShow('B')

    def AClassSlot(self):
        self.__divideRanksShow('A')

    def qualifiedProductSlot(self):
        self.__divideRanksShow('pass')

    def loadMarkedImageByDirSlot(self):
        path = self.data.loadMarkedImageByDir()
        if path != '':
            self.dataMarkOutputShow.appendPlainText('已选取文件夹：' + path)
        else:
            self.dataMarkOutputShow.appendPlainText('未选取目录')
    
    def clearDataMarkOutputShowSlot(self):
        self.dataMarkOutputShow.clear()
   
    def saveMarkedDatasetSlot(self):
        if self.data.image == None and self.data.label == None:
            self.dataMarkOutputShow.appendPlainText('请先选择载入打标数据方式')
        else:
            path = self.data.saveMarkedDataset()
            if path != None:
                self.dataMarkOutputShow.appendPlainText('文件保存完成：' + path)

    def loadUnMarkedDataByDirSlot(self):
        self.loadImagePath = self.data.loadUnMarkedDataByDir()

        if self.loadImagePath == '':
            self.dataMarkOutputShow.appendPlainText('未选取目录')
        else:
            self.dataMarkOutputShow.appendPlainText('目录位置' + self.loadImagePath)

    def startShowUnmarkedImageSlot(self):
        self.loadImagePath = self.loadImagePath
        if self.loadImagePath == '':
            self.dataMarkOutputShow.appendPlainText('请选择未标记图片路径！')
        elif self.matId == None or self.prodId == None:
            QtWidgets.QMessageBox.information(self, '提示', '请先选择物料和产品')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '请选择打标数据保存的路径')
            self.savePath = self.data.file.selectDirPath()
            if self.savePath == '':
                self.dataMarkOutputShow.appendPlainText('请选择一个打标数据保存路径')
            else:
                for fileName in os.listdir(self.loadImagePath):
                    if fileName != 'Thumbs.db':
                    # 避免将系统缩略图文件导入其中
                        self.imagePath.append(f'{self.loadImagePath}/{fileName}')
                        if len(self.imagePath) == 1:
                            qImg = self.data.imageShow(self.imagePath[self.imageCount])
                            self.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))
