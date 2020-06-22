from _date import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonHesapla.clicked.connect(self.hesapla)

    def hesapla(self):
        start=self.ui.dateStart.date()
        end=self.ui.dateEnd.date()
        now=QDate.currentDate()
        print(start,end,now,sep="\n")
        #print("{}".format(start.daysTo(now)))
        print(start.daysInMonth(),start.longMonthName(12))




app=QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())