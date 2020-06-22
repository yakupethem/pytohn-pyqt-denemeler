from _qlineedit import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  QIntValidator
import sys

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.lineEditSignalSlot.setEnabled(False)  #line edit i pasif yapmak için
        self.ui.lineEditSignalSlot.returnPressed.connect(self.tikla)  # enter e basıldığı zaman
        self.ui.lineEdit_sadeceTamsay.setValidator(QIntValidator(0,100,self))
        self.ui.lineEdit_sadeceoku.setText("sadece okunabilir")
        self.ui.lineEdit_sadeceoku.setReadOnly(True)
        self.ui.lineEdit.setText("123")
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.lineEditPlaceholder.setPlaceholderText("örn. cep no girin")
        self.ui.lineEdit_bilgi.setToolTip("bilgi girin")
        self.ui.lineEdit_surukle.setDragEnabled(True)
        self.ui.lineEdit_uzunluk.setMaxLength(9)
    def tikla(self):
        metin=self.ui.lineEditSignalSlot.text()
        meti_oku=self.ui.lineEdit_okuma.text()
        print(metin,meti_oku)
        self.ui.lineEdit_yazma.setText(metin+" "+meti_oku)
        self.ui.lineEditSignalSlot.clear()
        self.ui.lineEdit_okuma.clear()  #içerik temizleme


app=QtWidgets.QApplication(sys.argv)
uyg=myapp()
uyg.show()
sys.exit(app.exec_())