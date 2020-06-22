# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sayfalar_arasi_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ikinci_pencere(object):
    def setupUi(self, ikinci_pencere):
        ikinci_pencere.setObjectName("ikinci_pencere")
        ikinci_pencere.resize(627, 278)
        self.label = QtWidgets.QLabel(ikinci_pencere)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(ikinci_pencere)
        self.lineEdit.setGeometry(QtCore.QRect(210, 60, 311, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.buton_ekle = QtWidgets.QPushButton(ikinci_pencere)
        self.buton_ekle.setGeometry(QtCore.QRect(270, 140, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.buton_ekle.setFont(font)
        self.buton_ekle.setObjectName("buton_ekle")

        self.retranslateUi(ikinci_pencere)
        QtCore.QMetaObject.connectSlotsByName(ikinci_pencere)

    def retranslateUi(self, ikinci_pencere):
        _translate = QtCore.QCoreApplication.translate
        ikinci_pencere.setWindowTitle(_translate("ikinci_pencere", "Form"))
        self.label.setText(_translate("ikinci_pencere", "isim :"))
        self.buton_ekle.setText(_translate("ikinci_pencere", "ekle"))
