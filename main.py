import sys
sys.path.append('src')
from ui.ui_loginWindow import Ui_loginWindow
from ui.ui_mainWindow import Ui_mainWindow
from ui.uiLogic.stateWindow import StateWindow
from ui.uiLogic.prodMatManageWindow import prodMatManageWindow
from ui.uiLogic.manageWindow import ManageWindow
from ui.uiLogic.dataWindow import DataWindow
from func.mysql import Mysql
from PyQt5 import QtWidgets, QtCore
from ui.uiLogic.changeLocalUserPassword import ChangeLocalUserPassword

class MainWindow(QtWidgets.QWidget, Ui_mainWindow):
    toDataWindowSignal = QtCore.pyqtSignal()
    toLoginWindowSignal = QtCore.pyqtSignal()
    toProductManageWindowSignal = QtCore.pyqtSignal()
    toStateWindowSingal = QtCore.pyqtSignal()
    def __init__(self, userName):
        super().__init__()
        self.setupUi(self)

        self.userName = userName
        self.sql = Mysql()

        self.toDataWindowButton.clicked.connect(self.toDataWindowSlot)
        self.toProductManageWindowButton.clicked.connect(self.toProductManageWindowSlot)
        self.toStateWindowButton.clicked.connect(self.toStateWindowSlot)
        self.changeUserButton.clicked.connect(self.toLoginWindowSlot)
        self.changeUserPasswordButton.clicked.connect(self.changeUserPasswordSlot)

    def toDataWindowSlot(self):
        self.dataWindow = DataWindow(self.userName)
        self.dataWindow.show()
    
    def toLoginWindowSlot(self):
        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

    def toProductManageWindowSlot(self):
        self.prodMatManageWindow = prodMatManageWindow()
        self.prodMatManageWindow.show()
    
    def toStateWindowSlot(self):
        self.stateWindow = StateWindow()
        self.stateWindow.show()
    
    def changeUserPasswordSlot(self):
        self.changeLocalUserPassword = ChangeLocalUserPassword(self.userName)
        self.changeLocalUserPassword.show()

class VoidManageWindow(QtWidgets.QMainWindow):
    def __init__(self, sql):
        super().__init__()

        self.sql = Mysql()

        self.setWindowTitle('管理界面')
        self.resize(800, 640)
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.manageWindow = ManageWindow(self.sql)
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

        self.sql = Mysql()
        self.manageWindow = VoidManageWindow(self.sql)

        self.show()
        if self.sql.installed == False:
            reply = QtWidgets.QMessageBox.question(
                self, '警告！', '未安装数据库是否安装？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
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
        self.mainwindow = MainWindow(userName)
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
