from PyQt5 import QtWidgets, QtCore
import sys, os
sys.path.append('src')
from ui.ui_prodMatManageWindow import Ui_prodMatManageWindow

class productManageWindow(QtWidgets.QWidget, Ui_prodMatManageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = productManageWindow()
    window.show()
    sys.exit(app.exec_())