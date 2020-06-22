import sys
from PyQt5 import QtWidgets
from _raidobutton import Ui_MainWindow
from PyQt5.uic import loadUi

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #loadUi("_radiobutton.ui",self)

        self.ui.radioButtonturkiye.toggled.connect(self.sec)
        self.ui.radioButtonalmanya.toggled.connect(self.sec)
        self.ui.radioButtonazerbeycan.toggled.connect(self.sec)
        self.ui.radioButtonlise.toggled.connect(self.sec)
        self.ui.radioButtonuniversite.toggled.connect(self.sec)
        self.ui.radioButtonyukseklisans.toggled.connect(self.sec)


        self.ui.pushButtonulke.clicked.connect(self.tiklaulke)
        self.ui.pushButtonegitim.clicked.connect(self.tiklaegitim)

    def tiklaulke(self):
        items=self.ui.groupBoxulke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.labelulke.setText("seçilen üle: "+rb.text())
    def tiklaegitim(self):
        items=self.ui.groupBoxegitm.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.labelegitim.setText("seçilen eğitim: "+rb.text())


    def sec(self):
        rb= self.sender()
        if rb.isChecked():
            print(rb.text())



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=window()
    win.show()
    sys.exit(app.exec_())
app()




