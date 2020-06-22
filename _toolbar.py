# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_toolbar.ui'
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(470, 20, 321, 251))
        self.frame.setMaximumSize(QtCore.QSize(521, 291))
        self.frame.setStyleSheet("image: url(:/icon/icon/Turkey.ico);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(100, 100, 171, 131))
        self.frame_2.setStyleSheet("border-image: url(:/icon/icon/Turkey.ico);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/bird-red.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRed.setIcon(icon)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/bird-green.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGreen.setIcon(icon1)
        self.actionGreen.setObjectName("actionGreen")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        self.actionYellow.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/bird-yellow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYellow.setIcon(icon2)
        self.actionYellow.setObjectName("actionYellow")
        self.actionTurk = QtWidgets.QAction(MainWindow)
        self.actionTurk.setCheckable(True)
        self.actionTurk.setChecked(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/Turkey.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTurk.setIcon(icon3)
        self.actionTurk.setObjectName("actionTurk")
        self.toolBar.addAction(self.actionRed)
        self.toolBar.addAction(self.actionGreen)
        self.toolBar.addAction(self.actionYellow)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTurk)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionRed.setText(_translate("MainWindow", "kırmızı"))
        self.actionRed.setToolTip(_translate("MainWindow", "kırmızı kuş"))
        self.actionGreen.setText(_translate("MainWindow", "yeşik kuş"))
        self.actionGreen.setToolTip(_translate("MainWindow", "yeşil"))
        self.actionYellow.setText(_translate("MainWindow", "sarı kuş"))
        self.actionYellow.setToolTip(_translate("MainWindow", "sarı"))
        self.actionTurk.setText(_translate("MainWindow", "türk"))
        self.actionTurk.setToolTip(_translate("MainWindow", "türk bayrağı"))
import icon_rc
