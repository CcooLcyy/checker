from PyQt5 import QtWidgets, QtCore
import sys
sys.path.append('src')
from func.mysql import Mysql
from ui.ui_manageWindow import Ui_manageWindow

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