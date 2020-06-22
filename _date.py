# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_date.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(100, 220, 131, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setObjectName("timeEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(390, 230, 190, 79))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateTimeEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButtonHesapla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHesapla.setGeometry(QtCore.QRect(140, 360, 171, 71))
        self.pushButtonHesapla.setObjectName("pushButtonHesapla")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 100, 591, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateStart = QtWidgets.QDateEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateStart.sizePolicy().hasHeightForWidth())
        self.dateStart.setSizePolicy(sizePolicy)
        self.dateStart.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dateStart.setCalendarPopup(True)
        self.dateStart.setObjectName("dateStart")
        self.horizontalLayout_2.addWidget(self.dateStart)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEnd = QtWidgets.QDateEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEnd.sizePolicy().hasHeightForWidth())
        self.dateEnd.setSizePolicy(sizePolicy)
        self.dateEnd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dateEnd.setCalendarPopup(True)
        self.dateEnd.setObjectName("dateEnd")
        self.horizontalLayout.addWidget(self.dateEnd)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
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
        self.pushButtonHesapla.setText(_translate("MainWindow", "hesapla"))
