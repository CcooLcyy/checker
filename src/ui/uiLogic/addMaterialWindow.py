import sys
sys.path.append('src')
from ui.ui_addMaterialWindow import Ui_addMaterialWindow
from PyQt5 import QtWidgets

class AddMaterialWindow(QtWidgets.QWidget, Ui_addMaterialWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)