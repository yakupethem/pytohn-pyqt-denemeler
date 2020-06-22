from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUi
from hesapmakinesi import Ui_MainWindow


class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.hesapla)
        self.ui.pushButton_2.clicked.connect(self.hesapla)
        self.ui.pushButton_3.clicked.connect(self.hesapla)
        self.ui.pushButton_4.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        print(sender)
        result = 0
        if sender == "topla":
            result = int(self.ui.lineEdit.text()) + int(self.ui.lineEdit_2.text())
        elif sender == "çıkar":
            result = int(self.ui.lineEdit.text()) - int(self.ui.lineEdit_2.text())
        elif sender == "çarp":
            result = int(self.ui.lineEdit.text()) * int(self.ui.lineEdit_2.text())
        elif sender == "böl":
            result = int(self.ui.lineEdit.text()) / int(self.ui.lineEdit_2.text())

        self.ui.label_3.setText("sonuç : " + str(result))


def app():
    app = QApplication(sys.argv)
    win = myapp()
    win.show()
    sys.exit(app.exec())


app()
