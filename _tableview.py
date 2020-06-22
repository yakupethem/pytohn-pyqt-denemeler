# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_tableview.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 30, 431, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(500, 60, 421, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textisim = QtWidgets.QLineEdit(self.widget)
        self.textisim.setObjectName("textisim")
        self.gridLayout.addWidget(self.textisim, 0, 1, 1, 1)
        self.textfiyat = QtWidgets.QLineEdit(self.widget)
        self.textfiyat.setObjectName("textfiyat")
        self.gridLayout.addWidget(self.textfiyat, 1, 1, 1, 1)
        self.buttonSave = QtWidgets.QPushButton(self.widget)
        self.buttonSave.setObjectName("buttonSave")
        self.gridLayout.addWidget(self.buttonSave, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.buttonDel = QtWidgets.QPushButton(self.widget)
        self.buttonDel.setObjectName("buttonDel")
        self.gridLayout.addWidget(self.buttonDel, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonSave.setText(_translate("MainWindow", "kaydet"))
        self.label_2.setText(_translate("MainWindow", "isim"))
        self.label.setText(_translate("MainWindow", "fiyat"))
        self.buttonDel.setText(_translate("MainWindow", "sil"))
