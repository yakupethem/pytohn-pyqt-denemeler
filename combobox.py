from PyQt5.QtWidgets import *
import sys
from _combobox import *
from PyQt5.QtGui import QIcon

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboboxKus.addItem("kırmızı kuş",100)  #100 datası isteğe bağlıdır kullanıcı görmez arka planda kullanılır
        self.ui.comboboxKus.addItem(QIcon("icon/bird-green.ico"),"yeşil kuş")
        self.ui.comboboxKus.addItem(QIcon("icon/bird-yellow.ico"),"sarı kuş")
        self.ui.comboboxKus.insertItem(0,"seçiniz")  #en üste ekledik


        self.ui.comboboxAraba.addItems(["mercedes","BMW","audi","VW"])

        self.ui.comboboxmeyve.addItems(["seçiniz","elma","armut","muz"])

        self.ui.pushButtonSil.clicked.connect(self.Sil)
        self.ui.pushButtonGster.clicked.connect(self.goster)

#signal slot:
        #self.ui.comboboxmeyve.activated["int"].connect(self.meyveaktive)

        self.ui.comboboxmeyve.currentIndexChanged["int"].connect(self.change)
        self.ui.comboboxKus.currentIndexChanged["int"].connect(self.change)
        self.ui.comboboxAraba.currentIndexChanged["int"].connect(self.change)

        self.ui.comboboxAraba.currentIndexChanged["QString"].connect(self.changetext)
        self.ui.comboboxKus.currentIndexChanged["QString"].connect(self.changetext)
        self.ui.comboboxmeyve.currentIndexChanged["QString"].connect(self.changetext)

        self.ui.comboboxAraba.highlighted["int"].connect(self.high)

    def high(self,high):
        self.ui.statusbar.showMessage("seçim: "+str(high))

    def changetext(self,text):
        print("seçilen text: ",text)
        self.ui.label_2.setText("seçilen text: "+text)

    def change(self, index):
        if index != 0:
            print("seçilen index:",index)
            self.ui.label.setText("seçilen index: " + str(index))
            #print("seçilen text: ",self.ui.comboboxmeyve.currentText())
            #print("seçilen text: ", self.ui.comboboxKus.currentText())
            #print("seçilen text: ", self.ui.comboboxAraba.currentText())

    def meyveaktive(self,aktive_index):  #aynı şeyi seçtiğinde bile hep getirir
        print("aktif index:",aktive_index)
        print("aktive text:",self.ui.comboboxmeyve.itemText(aktive_index))
    def goster(self):
        kus_goster_text=self.ui.comboboxKus.currentText()
        kus_goster_index=self.ui.comboboxKus.currentIndex()
        kus_goster_data=self.ui.comboboxKus.currentData()
        kus_goster_item=self.ui.comboboxKus.itemText(kus_goster_index)  #int değer alır
        print("seçilen kuş: ",kus_goster_text)
        print("seçilen index: ",kus_goster_index)
        print("data: ",kus_goster_data)
        print("item_text: ",kus_goster_item)

    def Sil(self):
        self.ui.comboboxAraba.clear()  # içeriklerin hepsini siler
        self.ui.comboboxAraba.removeItem(0)  #seçileni siler
        self.ui.comboboxKus.clear()
        self.ui.comboboxmeyve.clear()





app=QApplication(sys.argv)
uyg = myapp()
uyg.show()
sys.exit(app.exec_())
