from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()

        self.setWindowTitle("pencere")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("Time.ico"))
        self.setToolTip("tool tip")
        self.ui()
    def ui(self):
        self.label=QLabel(self)
        self.label.move(50,30)
        self.label.setText("label: ")

        self.label2=QLabel(self)
        self.label2.move(100,110)
        self.label2.setText("label2")

        self.text=QLineEdit(self)
        self.text.move(100,30)

        self.buton=QPushButton(self)
        self.buton.move(100,70)
        self.buton.setText("buton")
        self.buton.clicked.connect(self.butonbas)

    def butonbas(self):
        self.label2.setText(self.text.text())

def window():
    app=QApplication(sys.argv)
    win=mywindow()
    win.show()
    sys.exit(app.exec())
window()

