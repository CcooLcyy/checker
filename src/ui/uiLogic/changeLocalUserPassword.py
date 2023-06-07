import sys
sys.path.append('src')
from PyQt5 import QtWidgets
from ui.ui_changeLocalUserPasswordWindow import Ui_changeLocalUserPassword
from func.mysql import Mysql

class ChangeLocalUserPassword(QtWidgets.QWidget, Ui_changeLocalUserPassword):
    def __init__(self, userName, sql):
        super().__init__()
        self.setupUi(self)

        self.sql = Mysql()
        self.userName = userName

        self.userNameShow.setText(self.userName)

        self.changePasswordButton.clicked.connect(self.changePasswordSlot)

    def changePasswordSlot(self):
        oldPasswordMd5 = self.sql.md5_encrypt(self.oldPassword.text())
        if oldPasswordMd5 == self.sql.verifyPassword(self.userName):
            if self.sql.md5_encrypt(self.newPassword.text()) == self.sql.md5_encrypt(self.newPasswordRe.text()):
                self.sql.changePassword(self.userName, self.newPassword.text())
                QtWidgets.QMessageBox.information(self, '提示', '密码修改成功')
                self.close()
            else:
                QtWidgets.QMessageBox.information(self, '提示', '两次密码输入不一致')
        else:
            QtWidgets.QMessageBox.information(self, '提示', '原密码输入错误')