import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QRasterWindow
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(400,400,700,400)
        self.gui()
    
    def gui(self):
        self.result = QtWidgets.QLabel(self)
        self.result.resize(350,70)
        self.result.move(210,50)

        self.one = QtWidgets.QPushButton(self)
        self.one.setText("1")
        self.one.resize(50,40)
        self.one.move(150,100)
        self.one.clicked.connect(lambda x : self.result.setText(self.result.text()+"1"))

        self.two = QtWidgets.QPushButton(self)
        self.two.setText("2")
        self.two.resize(50,40)
        self.two.move(210,100)
        self.two.clicked.connect(lambda x : self.result.setText(self.result.text()+"2"))

        self.three = QtWidgets.QPushButton(self)
        self.three.setText("3")
        self.three.resize(50,40)
        self.three.move(270,100)
        self.three.clicked.connect(lambda x : self.result.setText(self.result.text()+"3"))
        
        self.four = QtWidgets.QPushButton(self)
        self.four.setText("4")
        self.four.resize(50,40)
        self.four.move(150,150)
        self.four.clicked.connect(lambda x : self.result.setText(self.result.text()+"4"))
        
        self.five = QtWidgets.QPushButton(self)
        self.five.setText("5")
        self.five.resize(50,40)
        self.five.move(210,150)
        self.five.clicked.connect(lambda x : self.result.setText(self.result.text()+"5"))

        self.six = QtWidgets.QPushButton(self)
        self.six.setText("6")
        self.six.resize(50,40)
        self.six.move(270,150)
        self.six.clicked.connect(lambda x : self.result.setText(self.result.text()+"6"))

        self.seven = QtWidgets.QPushButton(self)
        self.seven.setText("7")
        self.seven.resize(50,40)
        self.seven.move(150,200)
        self.seven.clicked.connect(lambda x : self.result.setText(self.result.text()+"7"))

        self.eight = QtWidgets.QPushButton(self)
        self.eight.setText("8")
        self.eight.resize(50,40)
        self.eight.move(210,200)
        self.eight.clicked.connect(lambda x : self.result.setText(self.result.text()+"8"))

        self.nine = QtWidgets.QPushButton(self)
        self.nine.setText("9")
        self.nine.resize(50,40)
        self.nine.move(270,200)
        self.nine.clicked.connect(lambda x : self.result.setText(self.result.text()+"9"))

        self.zero = QtWidgets.QPushButton(self)
        self.zero.setText("0")
        self.zero.resize(50,40)
        self.zero.move(210,250)
        self.zero.clicked.connect(lambda x : self.result.setText(self.result.text()+"0"))

        self.plus = QtWidgets.QPushButton(self)
        self.plus.setText("+")
        self.plus.setStyleSheet("background-color : #ffcc99")
        self.plus.resize(50,40)
        self.plus.move(330,100)
        self.plus.clicked.connect(lambda x : self.result.setText(self.result.text()+" + "))

        self.minus = QtWidgets.QPushButton(self)
        self.minus.setText("-")
        self.minus.resize(50,40)
        self.minus.setStyleSheet("background-color : #ffcc99")
        self.minus.move(330,150)
        self.minus.clicked.connect(lambda x : self.result.setText(self.result.text()+" - "))


        self.divide = QtWidgets.QPushButton(self)
        self.divide.setText("/")
        self.divide.resize(50,40)
        self.divide.setStyleSheet("background-color : #ffcc99")
        self.divide.move(330,200)
        self.divide.clicked.connect(lambda x : self.result.setText(self.result.text()+" / "))

        self.multiply = QtWidgets.QPushButton(self)
        self.multiply.setText("*")
        self.multiply.resize(50,40)
        self.multiply.setStyleSheet("background-color : #ffcc99")
        self.multiply.move(330,250)
        self.multiply.clicked.connect(lambda x : self.result.setText(self.result.text()+" * "))

        self.equal =QtWidgets.QPushButton(self)
        self.equal.setText("=")
        self.equal.resize(50,40)
        self.equal.setStyleSheet("background-color : #ffcc99")
        self.equal.move(330,300)
        self.equal.clicked.connect(lambda x : self.result.setText(str(eval(self.result.text()))))
def start():
    app = QApplication(sys.argv)
    win = Calculator()

    win.show()
    sys.exit(app.exec())
start()
