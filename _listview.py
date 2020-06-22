# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_listview.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 30, 311, 451))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(420, 30, 181, 431))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_ekle = QtWidgets.QPushButton(self.widget)
        self.pushButton_ekle.setObjectName("pushButton_ekle")
        self.verticalLayout.addWidget(self.pushButton_ekle)
        self.pushButton_dzenle = QtWidgets.QPushButton(self.widget)
        self.pushButton_dzenle.setObjectName("pushButton_dzenle")
        self.verticalLayout.addWidget(self.pushButton_dzenle)
        self.pushButton_cikar = QtWidgets.QPushButton(self.widget)
        self.pushButton_cikar.setObjectName("pushButton_cikar")
        self.verticalLayout.addWidget(self.pushButton_cikar)
        self.pushButton_up = QtWidgets.QPushButton(self.widget)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(self.widget)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout.addWidget(self.pushButton_down)
        self.pushButton_sirala = QtWidgets.QPushButton(self.widget)
        self.pushButton_sirala.setObjectName("pushButton_sirala")
        self.verticalLayout.addWidget(self.pushButton_sirala)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout.addWidget(self.pushButton_exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 31))
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
        self.pushButton_ekle.setText(_translate("MainWindow", "ekle"))
        self.pushButton_dzenle.setText(_translate("MainWindow", "düzenle"))
        self.pushButton_cikar.setText(_translate("MainWindow", "çıkar"))
        self.pushButton_up.setText(_translate("MainWindow", "yukarı al"))
        self.pushButton_down.setText(_translate("MainWindow", "aşağı al"))
        self.pushButton_sirala.setText(_translate("MainWindow", "sırala"))
        self.pushButton_exit.setText(_translate("MainWindow", "çık"))
