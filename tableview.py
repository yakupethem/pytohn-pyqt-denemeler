from PyQt5.QtWidgets import *
from _tableview import Ui_MainWindow
import sys



class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.product()
        self.ui.buttonSave.clicked.connect(self.ekle)
        self.ui.buttonDel.clicked.connect(self.sil)

    def product(self):
        urunler=[
            {'isim':'samsung','fiyat':'2000'},
            {'isim': 'sony', 'fiyat': '3000'},
            {'isim': 'apple', 'fiyat': '4000'},
            {'isim': 'huawei', 'fiyat': '1000'}
                 ]
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(len(urunler))
        self.ui.tableWidget.setHorizontalHeaderLabels(("isim", "fiyat"))
        self.ui.tableWidget.setColumnWidth(0,200)
        self.ui.tableWidget.setColumnWidth(1, 50)
        row = 0
        for urun in urunler:
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(urun["isim"]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(urun["fiyat"])))
            row += 1

            # elle ekledik:
            """self.ui.tableWidget.setItem(1, 0, QTableWidgetItem("sony"))
            self.ui.tableWidget.setItem(1, 1, QTableWidgetItem("3000"))
            self.ui.tableWidget.setItem(2, 0, QTableWidgetItem("apple"))
            self.ui.tableWidget.setItem(2, 1, QTableWidgetItem("4000"))"""



    def ekle(self):
        isim = self.ui.textisim.text()
        fiyat = self.ui.textfiyat.text()
        if  isim and fiyat is not None:
            satir_sayisi=self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(satir_sayisi)
            self.ui.tableWidget.setItem(satir_sayisi,0,QTableWidgetItem(isim))
            self.ui.tableWidget.setItem(satir_sayisi,1,QTableWidgetItem(fiyat))

    def sil(self):
        sec=self.ui.tableWidget.selectedItems()
        for a in sec:
            self.ui.tableWidget.removeRow(a.row())



app=QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())