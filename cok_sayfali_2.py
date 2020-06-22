from PyQt5.QtWidgets import *
from _2sayfa import Ui_Form

class second(QWidget):
    def __init__(self):
        super(second, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
