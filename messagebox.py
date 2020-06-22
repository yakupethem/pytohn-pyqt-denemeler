from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from _messagebox import *

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCritical.clicked.connect(self.critical)
        self.ui.pushButtonInfo.clicked.connect(self.info)
        self.ui.pushButtonQuestion.clicked.connect(self.question)
        self.ui.pushButtonWarning.clicked.connect(self.warning)
        self.ui.pushButtonOzel.clicked.connect(self.ozel)
        self.ui.pushButtonAbautQT.clicked.connect(self.about)
        self.ui.pushButtonY40.clicked.connect(self.y40)

    def critical(self):
        sonuc=QMessageBox.critical(self,"başlık","critical",QMessageBox.Yes|QMessageBox.No)
        print(sonuc)

        if sonuc==QMessageBox.Yes:  #if sonuc==16384:
            print("evete basıldı")
        elif sonuc==QMessageBox.No:  #elif sonuc==65536
            print("hayıra basıldı")
    def info(self):
        QMessageBox.information(self,"bilgi","bilgi mesajı")
    def question(self):
        QMessageBox.question(self,"yardım","soru mesajı",QMessageBox.Save|QMessageBox.Open)
    def warning(self):
        QMessageBox.warning(self,"dikkat","emin misin?",QMessageBox.Yes|QMessageBox.No)
    def about(self):
        QMessageBox.aboutQt(self,"hakkında")
    def y40(self):
        QMessageBox.about(self,"hakkında","bu bir y40 çalışmasıdır."
                                          "<b> E-Mail: <b>"
                                          "<a href=\"yakocan40@gmail.com\">y40<\a>")
    def ozel(self):
        mesaj=QMessageBox()
        mesaj.setIcon(QMessageBox.Question)
        mesaj.setText("hangi sayıları istiyorsun?")
        mesaj.setWindowTitle("sayılar")
        mesaj.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        mesaj.setEscapeButton(QMessageBox.Yes)

        evet=mesaj.button(QMessageBox.Yes)
        evet.setText("tek sayılar")

        hayir=mesaj.button(QMessageBox.No)
        hayir.setText("çift sayılar")

        sonuc= mesaj.exec_()

        print(sonuc)

        start=2
        stop=50
        step=2

        if  sonuc==QMessageBox.Yes:
            start=1
        elif sonuc==QMessageBox.No:
            start=0

        self.ui.comboBox.clear()

        for i in  range(start,stop,step):
            self.ui.comboBox.addItem(str(i))




def app():
    uyg=QtWidgets.QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(uyg.exec_())
app()

