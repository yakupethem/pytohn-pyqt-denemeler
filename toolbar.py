from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from _toolbar import Ui_MainWindow
import sys

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionRed.triggered.connect(self.red)

    def red(self):
        self.ui.statusbar.showMessage("kırmızı kuş")
        self.ui.statusbar.setStyleSheet("color: rgb(255, 0, 4)")
        #self.ui.frame.setStyleSheet("border-image: url(:/icon/icon/bird-red.ico)")
        #self.frame.setStyleSheet("border-image: url(:/icon/icon/Turkey.ico);")
        self.frame.setStyleSheet("image: url(:/icon/icon/Turkey.ico);")


app=QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())
