from PyQt5.QtWidgets import *
from sayfalar_arasi_2 import Ui_ikinci_pencere
import sys
from PyQt5.QtCore import pyqtSignal

class myapp2(QWidget):

    yeni_signal=pyqtSignal(str)
    def __init__(self):
        super(myapp2, self).__init__()
        self.ui=Ui_ikinci_pencere()
        self.ui.setupUi(self)

        self.ui.buton_ekle.clicked.connect(self.ekle)

    def ekle(self):
        isim=self.ui.lineEdit.text()
        self.yeni_signal.emit(isim)
        self.ui.lineEdit.clear()




"""
app=QApplication([])
uyg=myapp2()
uyg.show()
app.exec_()"""