from PyQt5.QtWidgets import *
from _1sayfa import Ui_MainWindow
import sys
from cok_sayfali_2 import second
from cok_sayfali_3 import third

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buton2.clicked.connect(self.ikinci)
        self.ikici_Sayfa=second()

        self.ui.buton3.clicked.connect(self.ucuncu)
        self.ucuncu_sayfa=third()

    def ucuncu(self):
        self.ucuncu_sayfa.show()

    def ikinci(self):
        self.ikici_Sayfa.show()






app=QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())