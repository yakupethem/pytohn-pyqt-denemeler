from PyQt5.QtWidgets import *
from sayfalar_arasi_1 import Ui_ilk_pencere
from sayfalar_arasi_main2 import myapp2
import sys

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_ilk_pencere()
        self.ui.setupUi(self)

        self.main2=myapp2()
        self.main2.yeni_signal.connect(self.yeni_ekle)

        self.ui.buton_yenikisi.clicked.connect(self.yeni)
        self.ui.buton_yenikisi_2.clicked.connect(self.sil)

    def yeni_ekle(self, name):
        self.ui.comboBox.addItem(name)
        self.main2.close()
    def sil(self):
        a=self.ui.comboBox.currentIndex()
        b=self.ui.comboBox.removeItem(a)
        del b
    def yeni(self):
        self.main2.show()


app=QApplication([])
uyg=myapp()
uyg.show()
app.exec_()