from PyQt5  import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()

        self.setWindowTitle("ilk pecere")
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon("Time.ico"))
        self.setToolTip("tool tip")
        self.ui()
    def ui(self):
        self.lbl_name=QLabel(self)
        self.lbl_name.setText("adınız: ")
        self.lbl_name.move(50,30)

        self.txt_name=QLineEdit(self)
        self.txt_name.move(150,30)
        self.txt_name.resize(200,32)

        self.lbl_surname=QLabel(self)
        self.lbl_surname.setText("soyadınız: ")
        self.lbl_surname.move(50,70)

        self.txt_surname = QLineEdit(self)
        self.txt_surname.move(150, 70)
        self.txt_surname.resize(200, 32)

        self.sonuc=QLabel(self)
        self.sonuc.resize(300,50)
        self.sonuc.move(150,200)

        self.buton=QPushButton(self)
        self.buton.move(150,150)
        self.buton.setText("yazdır")
        self.buton.clicked.connect(self.click)

    def click(self):
        self.sonuc.setText("ad: "+self.txt_name.text()+" soyadınız: "+self.txt_surname.text())



def window():
    app =QApplication(sys.argv)
    win =mywindow()
    win.show()
    sys.exit(app.exec())

window()
