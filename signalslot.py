import sys
from PyQt5.QtWidgets import *
from _signalslot import *

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

uygulama=QApplication(sys.argv)
win=myapp()
win.show()
sys.exit(uygulama.exec())
