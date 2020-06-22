# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sayfalar_arasi_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ilk_pencere(object):
    def setupUi(self, ilk_pencere):
        ilk_pencere.setObjectName("ilk_pencere")
        ilk_pencere.resize(616, 324)
        self.centralwidget = QtWidgets.QWidget(ilk_pencere)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 100, 271, 51))
        self.comboBox.setObjectName("comboBox")
        self.buton_yenikisi = QtWidgets.QPushButton(self.centralwidget)
        self.buton_yenikisi.setGeometry(QtCore.QRect(370, 90, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buton_yenikisi.setFont(font)
        self.buton_yenikisi.setObjectName("buton_yenikisi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buton_yenikisi_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buton_yenikisi_2.setGeometry(QtCore.QRect(380, 170, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buton_yenikisi_2.setFont(font)
        self.buton_yenikisi_2.setObjectName("buton_yenikisi_2")
        ilk_pencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ilk_pencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 31))
        self.menubar.setObjectName("menubar")
        ilk_pencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ilk_pencere)
        self.statusbar.setObjectName("statusbar")
        ilk_pencere.setStatusBar(self.statusbar)

        self.retranslateUi(ilk_pencere)
        QtCore.QMetaObject.connectSlotsByName(ilk_pencere)

    def retranslateUi(self, ilk_pencere):
        _translate = QtCore.QCoreApplication.translate
        ilk_pencere.setWindowTitle(_translate("ilk_pencere", "MainWindow"))
        self.buton_yenikisi.setText(_translate("ilk_pencere", "yeni kişi"))
        self.label.setText(_translate("ilk_pencere", "kullanıcılar :"))
        self.buton_yenikisi_2.setText(_translate("ilk_pencere", "sil"))
