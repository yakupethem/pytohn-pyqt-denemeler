from PyQt5.QtWidgets import *
from _3sayfa import Ui_MainWindow

class third(QMainWindow):
    def __init__(self):
        super(third, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
