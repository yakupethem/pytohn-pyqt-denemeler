from _listview import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys


class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_ekle.clicked.connect(self.ekle)
        self.ui.pushButton_dzenle.clicked.connect(self.duzenle)
        self.ui.pushButton_cikar.clicked.connect(self.cikar)
        self.ui.pushButton_up.clicked.connect(self.up)
        self.ui.pushButton_down.clicked.connect(self.down)
        self.ui.pushButton_sirala.clicked.connect(self.sirala)
        self.ui.pushButton_exit.clicked.connect(self.exit)
        self.loadStudent()
    def loadStudent(self):

        self.ui.listWidget.addItems(["ali","veli","y40"])
        self.ui.listWidget.setCurrentRow(0)
    def ekle(self):
        text,ok=QInputDialog.getText(self,"ekle","öğrenci ismi")
        sec_sira=self.ui.listWidget.currentRow()
        if text and ok is not None:
            self.ui.listWidget.insertItem(sec_sira, text)
    def duzenle(self):
        sec_sira = self.ui.listWidget.currentRow()
        sec_kisi=self.ui.listWidget.item(sec_sira)

        if sec_kisi is not None:
            text,ok=QInputDialog.getText(self,"düzenle","öğrenci adı",QLineEdit.Normal,sec_kisi.text())
            if text and ok is not None:
                sec_kisi.setText(text)

    def cikar(self):
        sec_sira = self.ui.listWidget.currentRow()
        sec_kisi = self.ui.listWidget.item(sec_sira)
        if sec_kisi is None:
            return
        q=QMessageBox.question(self,"sil","silmek istiyor musunuz ? : "+sec_kisi.text(),QMessageBox.Yes|QMessageBox.No)
        if q ==QMessageBox.Yes:
            al=self.ui.listWidget.takeItem(sec_sira)
            del al
    def up(self):
        sec_sira = self.ui.listWidget.currentRow()
        if sec_sira>=1:
            sec_kisi=self.ui.listWidget.takeItem(sec_sira)
            self.ui.listWidget.insertItem(sec_sira-1,sec_kisi)
            self.ui.listWidget.setCurrentItem(sec_kisi)
    def down(self):
        sec_sira = self.ui.listWidget.currentRow()
        if sec_sira <= self.ui.listWidget.count()-1:
            sec_kisi = self.ui.listWidget.takeItem(sec_sira)
            self.ui.listWidget.insertItem(sec_sira + 1, sec_kisi)
            self.ui.listWidget.setCurrentItem(sec_kisi)
    def sirala(self):
        self.ui.listWidget.sortItems()
    def exit(self):
        quit()

app=QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())

