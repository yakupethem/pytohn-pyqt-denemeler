from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from _pushbutton import *
import sys

class myapp(QMainWindow):
    def __init__(self):
        super(myapp, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setText("buton")
        self.ui.pushButton_2.setIcon(QIcon(":/icon/icon/Baykuş.ico"))
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(0, 255, 179);")
        self.ui.pushButton.setToolTip("F6 ya bas")
        self.ui.pushButton.setShortcut(QKeySequence("F5"))
        self.ui.pushButton_2.setShortcut(QKeySequence(Qt.CTRL+Qt.Key_P))
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(64, 16, 255)")
        self.ui.pushButton_4.clicked.connect(self.tikla)
        self.ui.pushButton_3.clicked["bool"].connect(self.bas)
        self.ui.pushButton_2.pressed.connect(self.pressed)
        self.ui.pushButton_2.released.connect(self.relased)
        self.ui.pushButton_2.setCheckable(True)  #checkable etkin

    def pressed(self):
        self.ui.pushButton_2.setText("basılı")

    def relased(self):
        self.ui.pushButton_2.setText("basılı değil")

    def bas(self,durum):

        if durum:
            self.ui.pushButton_3.setText("stop")
        else:
            self.ui.pushButton_3.setText("start")
            self.ui.pushButton_3.setChecked(False)

    def tikla(self):
        self.ui.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 4)")


app=QApplication(sys.argv)
uyh=myapp()
uyh.show()
sys.exit(app.exec_())