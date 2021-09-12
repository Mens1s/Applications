import sys
from PyQt5 import QtWidgets
from page1 import Ui1_MainWindow
from page2 import Ui2_MainWindow
from page3 import Ui3_MainWindow
from datetime import date, datetime
import currency
from login import login

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui1 = Ui1_MainWindow()
        self.ui1.setupUi(self)

        now = datetime.now()

        all = currency.Currency.getAll()
        str_all = list(str(all).split(","))
        mainpageinformation = ""

        for num in range(1,len(str_all)):
            mainpageinformation  += (str_all[num]+"                  ")
            if (num)%6 == 0:
                mainpageinformation += "\n"
        print(mainpageinformation)

        self.ui1.liveCurr.setText("TIME : "+str(now)+"       This currency for American Dolar ($)"+"\n"+mainpageinformation)

        self.ui1.loginCustomer.clicked.connect(self.loginascustomer)
        self.ui1.loginAdmin.clicked.connect(self.loginasadmin)

    def loginascustomer(self):
        self.ui2 = Ui2_MainWindow()
        self.ui2.setupUi(self)
        self.ui2.login.clicked.connect(self.control)
        
    def control(self):
        self.id_customer = self.ui2.id.text()
        self.password_customer = self.ui2.password.text()
        result =  login(self.id_customer,self.password_customer)
        if result[0] == 1:
            self.ui3 = Ui3_MainWindow()
            self.ui3.setupUi(self)

            # self.ui3.details.setText("Welcome Mr/s {result[1]} \n Yo") I have very important job sorry codee
            self.ui3.takemoney.clicked.connect(self.takemoney)
            self.ui3.sendmoney.clicked.connect(self.sendmoney)
            self.ui3.buycurr.clicked.connect(self.buycurr)
            self.ui3.takeloan.clicked.connect(self.takeloan)
    
        else:
            self.ui2.result.setText("ID or Password is wrong!")

    def takemoney(self):
        pass

    def sendmoney(self):
        pass

    def buycurr(self):
        pass

    def takeloan(self):
        pass

    def loginasadmin(self):
        pass
def workIt():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec())
workIt()
