# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui2_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 619)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 255, 7, 255), stop:0.965909 rgba(212, 235, 0, 255), stop:0.98 rgba(110, 110, 110, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(340, 170, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setStyleSheet("\n"
"background-color: rgb(247, 255, 85);")
        self.id.setObjectName("id")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"background-color: rgb(247, 255, 85);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"background-color: rgb(247, 255, 85);")
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(340, 220, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("\n"
"background-color: rgb(247, 255, 85);")
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(430, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login.setStyleSheet("background-color: rgb(255, 243, 115);")
        self.login.setObjectName("login")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(250, 370, 371, 51))
        self.result.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 255, 7, 255), stop:0.965909 rgba(212, 235, 0, 255), stop:0.98 rgba(110, 110, 110, 255))")
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID NUMBER :"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD :"))
        self.login.setText(_translate("MainWindow", "LOGIN"))
