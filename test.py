import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("src/ui/loginWindow.ui", self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()

        if email == "test" and password == "test":
            # Show main window
            widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        # Show create account window
        creatacc = CreateAcc()
        widget.addWidget(creatacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("createacc.ui", self)
        self.signupButton.clicked.connect(self.signupfunction)

    def signupfunction(self):
        email = self.email.text()
        if email == "test":
            print("Account created successfully")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

# Main
app = QApplication(sys.argv)
mainwindow = QDialog()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(400)
widget.setFixedWidth(300)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")