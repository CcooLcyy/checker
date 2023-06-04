import sys
sys.path.append('src')
from ui.ui_loginWindow import Ui_loginWindow
from ui.uiLogic.stateWindow import StateWindow
from ui.uiLogic.prodMatManageWindow import prodMatManageWindow
from ui.uiLogic.manageWindow import ManageWindow
from ui.uiLogic.dataWindow import DataWindow
from ui.uiLogic.mainWindow import MainWindow
from func.mysql import Mysql
from PyQt5 import QtWidgets


class VoidMainWindow(QtWidgets.QMainWindow):
    def __init__(self, userName, sql):
        super().__init__()
        self.setWindowTitle('主界面')
        self.resize(800, 640)
        self.userName = userName
        self.sql = sql

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        self.mainWindow = MainWindow(self.userName)
        self.dataWindow = DataWindow(self.userName, self.sql)
        self.prodMatManageWindow = prodMatManageWindow(self.sql)
        self.stateWindow = StateWindow(self.sql)
        self.stackedWidget.addWidget(self.mainWindow)
        self.stackedWidget.addWidget(self.dataWindow)
        self.stackedWidget.addWidget(self.prodMatManageWindow)
        self.stackedWidget.addWidget(self.stateWindow)

        self.mainWindow.toDataWindowSignal.connect(self.toDataWindowSlot)
        self.mainWindow.toLoginWindowSignal.connect(self.toLoginWindowSlot)
        self.mainWindow.toProductManageWindowSignal.connect(
            self.toProductManageWindowSlot)
        self.mainWindow.toStateWindowSingal.connect(self.toStateWindowSlot)
        self.dataWindow.toMainWindowSignal.connect(self.toMainWindowSlot)
        self.dataWindow.toProductManageWindowSignal.connect(
            self.toProductManageWindowSlot)
        self.dataWindow.toStateWindowSingal.connect(self.toStateWindowSlot)
        self.prodMatManageWindow.toMainWindowSignal.connect(
            self.toMainWindowSlot)
        self.prodMatManageWindow.toDataWindowSignal.connect(
            self.toDataWindowSlot)
        self.prodMatManageWindow.toStateWindowSingal.connect(
            self.toStateWindowSlot)
        self.stateWindow.toMainWindowSignal.connect(self.toMainWindowSlot)
        self.stateWindow.toDataWindowSignal.connect(self.toDataWindowSlot)
        self.stateWindow.toProdMatManageWindowSignal.connect(
            self.toProductManageWindowSlot)

    def toMainWindowSlot(self):
        self.stackedWidget.setCurrentIndex(0)

    def toDataWindowSlot(self):
        self.stackedWidget.setCurrentIndex(1)

    def toProductManageWindowSlot(self):
        self.stackedWidget.setCurrentIndex(2)

    def toStateWindowSlot(self):
        self.stackedWidget.setCurrentIndex(3)

    def toLoginWindowSlot(self):
        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()


class VoidManageWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('管理界面')
        self.resize(800, 640)
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

        self.sql = Mysql()
        self.manageWindow = VoidManageWindow()

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
        self.mainwindow = VoidMainWindow(userName, self.sql)
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
