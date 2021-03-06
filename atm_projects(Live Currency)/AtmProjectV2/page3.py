# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen/page3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui3_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 670)
        MainWindow.setStyleSheet("background-color: rgb(255, 216, 20);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendmoney = QtWidgets.QPushButton(self.centralwidget)
        self.sendmoney.setGeometry(QtCore.QRect(60, 190, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sendmoney.setFont(font)
        self.sendmoney.setStyleSheet("background-color: rgb(255, 131, 133);")
        self.sendmoney.setObjectName("sendmoney")
        self.takeloan = QtWidgets.QPushButton(self.centralwidget)
        self.takeloan.setGeometry(QtCore.QRect(60, 270, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takeloan.setFont(font)
        self.takeloan.setStyleSheet("background-color: rgb(255, 131, 133);")
        self.takeloan.setObjectName("takeloan")
        self.takemoney = QtWidgets.QPushButton(self.centralwidget)
        self.takemoney.setGeometry(QtCore.QRect(60, 110, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.takemoney.setFont(font)
        self.takemoney.setStyleSheet("background-color: rgb(255, 131, 133);")
        self.takemoney.setObjectName("takemoney")
        self.details = QtWidgets.QLabel(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(530, 80, 281, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.details.setFont(font)
        self.details.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.details.setMouseTracking(False)
        self.details.setText("")
        self.details.setObjectName("details")
        self.takerid = QtWidgets.QLineEdit(self.centralwidget)
        self.takerid.setEnabled(False)
        self.takerid.setGeometry(QtCore.QRect(570, 310, 241, 31))
        self.takerid.setObjectName("takerid")
        self.takeridtext = QtWidgets.QLabel(self.centralwidget)
        self.takeridtext.setEnabled(False)
        self.takeridtext.setGeometry(QtCore.QRect(420, 310, 131, 31))
        self.takeridtext.setText("")
        self.takeridtext.setObjectName("takeridtext")
        self.amount_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.amount_2.setEnabled(False)
        self.amount_2.setGeometry(QtCore.QRect(570, 350, 241, 31))
        self.amount_2.setObjectName("amount_2")
        self.amounttext = QtWidgets.QLabel(self.centralwidget)
        self.amounttext.setEnabled(False)
        self.amounttext.setGeometry(QtCore.QRect(420, 350, 131, 31))
        self.amounttext.setText("")
        self.amounttext.setObjectName("amounttext")
        self.okey = QtWidgets.QPushButton(self.centralwidget)
        self.okey.setEnabled(False)
        self.okey.setGeometry(QtCore.QRect(680, 400, 131, 51))
        font = QtGui.QFont()
        font.setKerning(True)
        self.okey.setFont(font)
        self.okey.setMouseTracking(True)
        self.okey.setText("")
        self.okey.setObjectName("okey")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(510, 470, 301, 41))
        self.result.setText("")
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
        self.sendmoney.setText(_translate("MainWindow", "SEND MONEY"))
        self.takeloan.setText(_translate("MainWindow", "TAKE LOAN"))
        self.takemoney.setText(_translate("MainWindow", "TAKE MONEY"))
