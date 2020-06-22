# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHobi = QtWidgets.QPushButton(self.centralwidget)
        self.btnHobi.setGeometry(QtCore.QRect(130, 310, 112, 34))
        self.btnHobi.setObjectName("btnHobi")
        self.lblSonuc = QtWidgets.QLabel(self.centralwidget)
        self.lblSonuc.setGeometry(QtCore.QRect(70, 410, 261, 81))
        self.lblSonuc.setText("")
        self.lblSonuc.setObjectName("lblSonuc")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(50, 40, 351, 231))
        self.groupHobiler.setObjectName("groupHobiler")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupHobiler)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitapOkuma = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbKitapOkuma.setObjectName("cbKitapOkuma")
        self.verticalLayout.addWidget(self.cbKitapOkuma)
        self.cbSpor = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(410, 40, 351, 231))
        self.groupDersler.setObjectName("groupDersler")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupDersler)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 20, 221, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbSinema_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cbSinema_2.setObjectName("cbSinema_2")
        self.verticalLayout_2.addWidget(self.cbSinema_2)
        self.cbKitapOkuma_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cbKitapOkuma_2.setObjectName("cbKitapOkuma_2")
        self.verticalLayout_2.addWidget(self.cbKitapOkuma_2)
        self.cbSpor_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cbSpor_2.setObjectName("cbSpor_2")
        self.verticalLayout_2.addWidget(self.cbSpor_2)
        self.btnDers = QtWidgets.QPushButton(self.centralwidget)
        self.btnDers.setGeometry(QtCore.QRect(470, 310, 112, 34))
        self.btnDers.setObjectName("btnDers")
        self.lblSonuc_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblSonuc_2.setGeometry(QtCore.QRect(430, 410, 261, 81))
        self.lblSonuc_2.setText("")
        self.lblSonuc_2.setObjectName("lblSonuc_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.btnHobi.setText(_translate("MainWindow", "seçilenleri al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "hobiler"))
        self.cbSinema.setText(_translate("MainWindow", "sinema"))
        self.cbKitapOkuma.setText(_translate("MainWindow", "kitap okuma"))
        self.cbSpor.setText(_translate("MainWindow", "spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "dersler"))
        self.cbSinema_2.setText(_translate("MainWindow", "matematik"))
        self.cbKitapOkuma_2.setText(_translate("MainWindow", "fizik"))
        self.cbSpor_2.setText(_translate("MainWindow", "edebiyat"))
        self.btnDers.setText(_translate("MainWindow", "seçilenleri al"))
