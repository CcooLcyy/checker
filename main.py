from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap
import sys, os
sys.path.append('src')
from func.data import Data
from func.file import File
from func.mysql import Mysql
from ui.ui_mainWindow import Ui_mainWindow
from ui.ui_dataWindow import Ui_dataPageWindow
from ui.ui_loginWindow import Ui_loginWindow
from ui.ui_manageWindow import Ui_manageWindow

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    toLoginWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.changeUserButton.clicked.connect(self.toLoginWindowSlot)

    def toDataWindowSlot(self):
        self.toDataWindowSignal.emit()
    
    def toLoginWindowSlot(self):
        self.toLoginWindowSignal.emit()

class DataWindow(QtWidgets.QWidget, Ui_dataPageWindow):
    toMainWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = Data()
        self.file = File()
        self.imagePath = []
        self.imageCount = 0
        self.loadImagePath = ''
        self.savePath = ''
        
        self.toMainWindowButton.clicked.connect(self.toMainWindowSlot)
        self.loadMarkedImageByDir.clicked.connect(self.loadMarkedImageByDirSlot)
        self.clearDataMarkOutputShowButton.clicked.connect(self.clearDataMarkOutputShowSlot)
        self.clearDatasetCollectOutputShow.clicked.connect(self.clearDatasetCollectOutputShowSlot)
        self.saveMarkedDataset.clicked.connect(self.saveMarkedDatasetSlot)
        self.loadUnMarkedDataByDir.clicked.connect(self.loadUnMarkedDataByDirSlot)
        self.startShowUnmarkedImageButton.clicked.connect(self.startShowUnmarkedImageSlot)
        self.qualifiedProductButton.clicked.connect(self.qualifiedProductSlot)
        self.AClassButton.clicked.connect(self.AClassSlot)
        self.BClassButton.clicked.connect(self.BClassSlot)
        self.CClassButton.clicked.connect(self.CClassSlot)

    def divideRanksShow(self, mark):
        if len(self.imagePath) == 0:
            self.dataMarkOutputShow.appendPlainText('请先点击开始打标')
        else:
            if self.imageCount >= len(self.imagePath):
                self.dataMarkOutputShow.appendPlainText('图片打标已完成，请重新选择数据')
            else:
                filePath = self.imagePath[self.imageCount]
                self.file.renameData(filePath, self.savePath, mark)
                self.imageCount += 1
                if self.imageCount >= len(self.imagePath):
                    self.dataMarkOutputShow.appendPlainText('图片打标完成')
                    self.UnmarkedImageShow.clear()
                else:
                    qImg = self.data.imageShow(self.imagePath[self.imageCount])
                    self.UnmarkedImageShow.setPixmap(QPixmap.fromImage(qImg))

    def CClassSlot(self):
        self.divideRanksShow('C')

    def BClassSlot(self):
        self.divideRanksShow('B')

    def AClassSlot(self):
        self.divideRanksShow('A')

    def qualifiedProductSlot(self):
        self.divideRanksShow('pass')

    def toMainWindowSlot(self):
        self.toMainWindowSignal.emit()

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

    def startShowUnmarkedImageSlot(self):
        self.loadImagePath = self.loadImagePath
        if self.loadImagePath == '':
            self.dataMarkOutputShow.appendPlainText('请选择未标记图片路径！')
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

class VoidMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主界面')
        self.resize(1000, 800)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.mainWindow = MainWindow()
        self.dataWindow = DataWindow()
        self.stackedWidget.addWidget(self.mainWindow)
        self.stackedWidget.addWidget(self.dataWindow)

        self.mainWindow.toDataWindowSignal.connect(self.toDataWindowSlot)
        self.mainWindow.toLoginWindowSignal.connect(self.toLoginWindowSlot)
        self.dataWindow.toMainWindowSignal.connect(self.toMainWindowSlot)

    def toMainWindowSlot(self):
        self.stackedWidget.setCurrentIndex(0)

    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(1)

    def toLoginWindowSlot(self):
        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

class ManageWindow(QtWidgets.QWidget, Ui_manageWindow):
    toLoginWindowSignal = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sql = Mysql()

        self.changeUserButton.clicked.connect(self.changeUserSlot)
        self.addUserButton.clicked.connect(self.addUserSlot)
        self.clearManageInfoShowButton.clicked.connect(self.manageInfoShow.clear)
        self.changePasswordButton.clicked.connect(self.changeUserPasswordSlot)
        self.queryUserButton.clicked.connect(self.queryAllUserSlot)
        self.deleteUserButton.clicked.connect(self.deleteUserSlot)
        self.deleteUserButton.clicked.connect(self.deleteUserEdit.clear)

    def changeUserSlot(self):
        self.toLoginWindowSignal.emit()
    
    def addUserSlot(self):
        userName = self.addUserNameEdit.text()
        userPassword = self.addUserPasswordEdit.text()
        if userName == '':
            self.manageInfoShow.appendPlainText('请输入用户名')
        else:
            show = self.sql.addUser(userName, userPassword)
            self.manageInfoShow.appendPlainText(show)

    def changeUserPasswordSlot(self):
        userName = self.changeUserNameEdit.text()
        userPassword = self.changeUserPasswordEdit.text()
        if userName == '':
            self.manageInfoShow.appendPlainText('请正确输入用户名密码！')
        else:
            infoShow = self.sql.changePassword(userName, userPassword)
            self.manageInfoShow.appendPlainText(infoShow)

    def queryAllUserSlot(self):
        result = self.sql.queryAllUser()
        for _ in result:
            self.manageInfoShow.appendPlainText(f'{_[0]}')
    
    def deleteUserSlot(self):
        deleteUserName = self.deleteUserEdit.text()
        if deleteUserName == 'admin':
            self.manageInfoShow.appendPlainText('无法删除“admin”用户！')
            self.deleteUserEdit.clear()
        elif deleteUserName == '':
            self.manageInfoShow.appendPlainText('请正确输入待删除用户')
        else:
            self.sql.deleteUser(deleteUserName)
            self.manageInfoShow.appendPlainText(f'用户：{deleteUserName}已删除')



class VoidManageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('管理界面')
        self.resize(1000, 800)
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.manageWindow = ManageWindow()
        self.stackedWidget.addWidget(self.manageWindow)

        self.manageWindow.toLoginWindowSignal.connect(self.toLoginWindowSlot)

    def toLoginWindowSlot(self):
        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

class LoginWindow(QtWidgets.QDialog, Ui_loginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainwindow = VoidMainWindow()
        self.manageWindow = VoidManageWindow()
        self.sql = Mysql()

        self.show()
        if self.sql.installed == False:
            reply = QtWidgets.QMessageBox.question(self, '警告！', '未安装数据库是否安装？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                QtWidgets.QMessageBox.information(self, '提示', '请选择安装位置！')
                # self.sql.installMysql()
                # 安装数据库流程
                QtWidgets.QMessageBox.information(self, '提示', '安装完成，请登录')
            elif reply == QtWidgets.QMessageBox.No:
                exit()

        self.loginButton.clicked.connect(self.loginSlot)
        self.cancelButton.clicked.connect(self.close)

    def loginSlot(self):
        userName = self.userNameEdit.text()
        password = self.passwordEdit.text()
        passwordMd5 = self.sql.md5_encrypt(password)
        if userName == '' or password == '':
            QtWidgets.QMessageBox.information(self, '警告！', '请输入账号密码！')
        elif passwordMd5 != self.sql.verifyPassword(userName):
            QtWidgets.QMessageBox.information(self, '警告！', '账号或密码错误')
        elif userName == 'admin' and passwordMd5 == self.sql.verifyPassword(userName):
            self.close()
            self.manageWindow.show()
        elif passwordMd5 == self.sql.verifyPassword(userName):
            self.close()
            self.mainwindow.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())