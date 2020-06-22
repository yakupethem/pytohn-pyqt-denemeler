import sys
from PyQt5 import QtWidgets
from _checkebox import Ui_MainWindow

class myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbKitapOkuma.stateChanged.connect(self.goster)
        self.ui.cbSpor.stateChanged.connect(self.goster)
        self.ui.cbSinema.stateChanged.connect(self.goster)

        self.ui.btnHobi.clicked.connect(self.SecAlHobi)
        self.ui.btnDers.clicked.connect(self.SecAlDers)

    def SecAlHobi(self):
        result=""
        items=self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox)
        for item in items:
            if item.isChecked():
                result += item.text() + "\n"
        self.ui.lblSonuc.setText("seçilen habiler:"+str(result))

    def SecAlDers(self):
            result = ""
            items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
            for item in items:
                if item.isChecked():
                    result += item.text() + "\n"
            self.ui.lblSonuc_2.setText("dersler: "+str(result))

                #print(item.text())
                #print(item.isChecked())

    def goster(self, value):

        cb=self.sender()
        print(cb.text())
        print(cb.isChecked())
        print(value)
        #print(self.ui.cbKitapOkuma.isChecked())
        #print(self.ui.cbKitapOkuma.text())



def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myapp()
    win.show()
    sys.exit(app.exec_())
app()