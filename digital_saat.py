from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class clock(QWidget):
    def __init__(self):
        super(clock,self).__init__()
        self.pencere=loadUi("untitled.ui",self)
        self.gosterge=self.pencere.lcdNumber
        self.gosterge.setSegmentStyle(QLCDNumber.Filled)
        zaman=QTimer(self)
        zaman.timeout.connect(self.zamangoster)
        zaman.start(1000)
        self.zamangoster()
        #self.setWindowTitle("Dijital Saat")
        self.setWindowIcon(QIcon(":/icon/Desktop/icon/Clock.ico"))
        

    def zamangoster(self):
        simdi=QTime.currentTime()
        metin=simdi.toString("hh:mm")
        print(metin)
        if (simdi.second() % 2) == 0:
            metin = metin[:2] + " " + metin[3:]
        self.gosterge.display(metin)





uygulama=QApplication(sys.argv)
saat=clock()
saat.show()
uygulama.exec()
