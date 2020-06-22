# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_radiobutton.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxulke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxulke.setGeometry(QtCore.QRect(40, 50, 401, 251))
        self.groupBoxulke.setObjectName("groupBoxulke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxulke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 381, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutulke = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutulke.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutulke.setObjectName("gridLayoutulke")
        self.radioButtonturkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButtonturkiye.setObjectName("radioButtonturkiye")
        self.gridLayoutulke.addWidget(self.radioButtonturkiye, 0, 0, 1, 1)
        self.radioButtonazerbeycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButtonazerbeycan.setObjectName("radioButtonazerbeycan")
        self.gridLayoutulke.addWidget(self.radioButtonazerbeycan, 3, 0, 1, 1)
        self.radioButtonalmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButtonalmanya.setObjectName("radioButtonalmanya")
        self.gridLayoutulke.addWidget(self.radioButtonalmanya, 2, 0, 1, 1)
        self.groupBoxegitm = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxegitm.setGeometry(QtCore.QRect(510, 70, 421, 231))
        self.groupBoxegitm.setObjectName("groupBoxegitm")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxegitm)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 381, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutegitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutegitim.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutegitim.setObjectName("gridLayoutegitim")
        self.radioButtonlise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButtonlise.setObjectName("radioButtonlise")
        self.gridLayoutegitim.addWidget(self.radioButtonlise, 0, 0, 1, 1)
        self.radioButtonyukseklisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButtonyukseklisans.setObjectName("radioButtonyukseklisans")
        self.gridLayoutegitim.addWidget(self.radioButtonyukseklisans, 3, 0, 1, 1)
        self.radioButtonuniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButtonuniversite.setObjectName("radioButtonuniversite")
        self.gridLayoutegitim.addWidget(self.radioButtonuniversite, 2, 0, 1, 1)
        self.pushButtonulke = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonulke.setGeometry(QtCore.QRect(140, 360, 201, 71))
        self.pushButtonulke.setObjectName("pushButtonulke")
        self.pushButtonegitim = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonegitim.setGeometry(QtCore.QRect(560, 360, 201, 71))
        self.pushButtonegitim.setObjectName("pushButtonegitim")
        self.labelulke = QtWidgets.QLabel(self.centralwidget)
        self.labelulke.setGeometry(QtCore.QRect(140, 500, 291, 121))
        self.labelulke.setText("")
        self.labelulke.setObjectName("labelulke")
        self.labelegitim = QtWidgets.QLabel(self.centralwidget)
        self.labelegitim.setGeometry(QtCore.QRect(630, 490, 311, 101))
        self.labelegitim.setText("")
        self.labelegitim.setObjectName("labelegitim")
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
        self.groupBoxulke.setTitle(_translate("MainWindow", "ülkeler"))
        self.radioButtonturkiye.setText(_translate("MainWindow", "türkiye"))
        self.radioButtonazerbeycan.setText(_translate("MainWindow", "azerbeycan"))
        self.radioButtonalmanya.setText(_translate("MainWindow", "almanya"))
        self.groupBoxegitm.setTitle(_translate("MainWindow", "eğitim"))
        self.radioButtonlise.setText(_translate("MainWindow", "lise"))
        self.radioButtonyukseklisans.setText(_translate("MainWindow", "yüksek lisans"))
        self.radioButtonuniversite.setText(_translate("MainWindow", "üniversite"))
        self.pushButtonulke.setText(_translate("MainWindow", "ülke seçimi"))
        self.pushButtonegitim.setText(_translate("MainWindow", "eğitim seçimi"))
