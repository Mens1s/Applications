import sys
from PyQt5 import QtWidgets
from page1 import Ui1_MainWindow
from page2 import Ui2_MainWindow
from page3 import Ui3_MainWindow
from page4 import Ui4_MainWindow
from page5 import Ui5_MainWindow
from datetime import datetime
import currency
import json
from login import login
from login import controlUser

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui1 = Ui1_MainWindow()
        self.ui1.setupUi(self)

        now = datetime.now()

        all = currency.Currency.getAll()
        str_all = list(str(all).split(","))


        for num in range(1,len(str_all)):
            self.ui1.listWidget.addItem(str(str_all[num]))

        self.ui1.loginCustomer.clicked.connect(self.loginascustomer)
        self.ui1.loginAdmin.clicked.connect(self.loginasadmin)

    def loginascustomer(self):
        self.ui2 = Ui2_MainWindow()
        self.ui2.setupUi(self)
        self.ui2.login.clicked.connect(self.control)
        
    def control(self):
        if self.ui2.password.text() is None or self.ui2.id.text() is None:
            self.password_customer = "1"
            self.id_customer = "1"
        else:
            self.password_customer = str(self.ui2.password.text())
            self.id_customer = str(self.ui2.id.text())
        self.result =  login(self.id_customer,self.password_customer)
        if self.result[0] == 1:
            self.ui3 = Ui3_MainWindow()
            self.ui3.setupUi(self)
            currencyBalance = dict(self.result[4])
            self.text = ""
            for a in currencyBalance:
                self.text += " "+a+ " = " +currencyBalance[a]+"\n"
            self.ui3.details.setText(f" Welcome Mr/s {self.result[1]} \n Your balance : {self.result[3]} \n Your currency balance is : \n {self.text}") 
            self.ui3.takemoney.clicked.connect(self.takemoney)
            self.ui3.sendmoney.clicked.connect(self.sendmoney)
            self.ui3.takeloan.clicked.connect(self.takeloan)
    
        else:
            self.ui2.result.setText("ID or Password is wrong!")

    def takemoney(self):
        self.ui3.takeridtext.setText("Amounts of Money : ")
        self.ui3.amounttext.setText("Enter Password : ")

        self.ui3.okey.setEnabled(True)
        self.ui3.takerid.setEnabled(True)
        self.ui3.amount_2.setEnabled(True)
        self.ui3.okey.clicked.connect(self.controlTake)

    def controlTake(self):
        if int(self.ui3.takerid.text()) <= int(self.result[3]):
            if self.ui3.amount_2.text() == self.password_customer:
                new_balance = int(self.result[3])-int(self.ui3.takerid.text())

                with open("data.json","r") as old_data:
                    self.old_data = json.load(old_data)

                self.old_data[self.id_customer]["tr_balance"] = str(new_balance)

                with open("data.json","w") as new_data:
                    new_data.write(json.dumps(self.old_data))

                self.ui3.details.setText(f" Welcome Mr/s {self.result[1]} \n Your balance : {new_balance} \n Your currency balance is : \n {self.text}")

                self.ui3.okey.setEnabled(False) #I did it because every clicking  will take money from balance.

                self.ui3.result.setText("Your order succesfully proccesed!")

                while True:
                    QtWidgets.QMessageBox.about(self,"Exit",f"Your order succesfully proccesed.\nYou will be log out.\n       Press okey button.")
                    sys.exit()

            else:
                self.ui3.result.setText("Your Password is wrong!")
        else:
            self.ui3.result.setText("Your balance is not enough! ")
    def sendmoney(self):
        self.ui3.takeridtext.setText("Taker ID : ")
        self.ui3.amounttext.setText("Amounts of Money : ")

        self.ui3.okey.setEnabled(True)
        self.ui3.takerid.setEnabled(True)
        self.ui3.amount_2.setEnabled(True)

        self.ui3.okey.clicked.connect(self.controlSend)


    def controlSend(self):
        if int(self.ui3.amount_2.text()) <= int((self.result[3])):
            if controlUser(self.ui3.takerid.text())==1: 
                new_balance = int(self.result[3]) - int(self.ui3.amount_2.text())

                with open("data.json","r") as old_data:
                    self.old_data = json.load(old_data)
            
                self.old_data[self.ui3.takerid.text()]["tr_balance"] = str(int(self.old_data[self.ui3.takerid.text()]["tr_balance"])+int(self.ui3.amount_2.text()))
                self.old_data[self.id_customer]["tr_balance"] = str(new_balance)

                with open("data.json","w") as data:
                    data.write(json.dumps(self.old_data))

                self.ui3.details.setText(f" Welcome Mr/s {self.result[1]} \n Your balance : {new_balance} \n Your currency balance is : \n {self.text}")

                self.ui3.okey.setEnabled(False) 

                self.ui3.result.setText("Your order succesfully proccesed.")
                while True:
                    QtWidgets.QMessageBox.about(self,"Exit",f"Your order succesfully proccesed.\nYou will be log out.\n        Press okey button.")
                    sys.exit()
            else:

                self.ui3.result.setText("Taker id is wrong!")
        else:
            self.ui3.result.setText("You do not have enough money!")

    def takeloan(self):
        self.ui3.takeridtext.setText("Amounts of Money : ")
        self.ui3.amounttext.setText("Password : ")

        self.ui3.okey.setEnabled(True)
        self.ui3.takerid.setEnabled(True)
        self.ui3.amount_2.setEnabled(True)

        self.ui3.okey.clicked.connect(self.controlLoan)
    
    def controlLoan(self):
        if self.ui3.amount_2.text()==self.password_customer:
            with open("loan.json","r") as loan:
                self.oldloan = json.load(loan)
                self.oldloan[self.id_customer]=self.ui3.takerid.text()
            with open("loan.json","w") as loan:
                
                loan.write(json.dumps(self.oldloan)+"\n")
        
            self.ui3.result.setText("Your wish was sent to manager.")
            self.ui3.okey.setEnabled(False)
            while True:
                    QtWidgets.QMessageBox.about(self,"Exit",f"Your order succesfully proccesed.\nYou will be log out.\n       Press okey button.")
                    sys.exit()

        else:
            self.ui3.result.setText("Your password is wrong!")
            
    def loginasadmin(self):
        self.ui4 = Ui4_MainWindow()
        self.ui4.setupUi(self)

        self.ui4.pushButton.clicked.connect(self.loginasadmincontrol)

    def loginasadmincontrol(self):
        if self.ui4.lineEdit.text() == "adminpassword":
            self.ui5 = Ui5_MainWindow()
            self.ui5.setupUi(self)

            totalmoney = 0
            totalloan = 0
            with open("data.json","r") as money:
                money = json.load(money)
                item = ""
                for b in money:
                    item = money[b]["name"]+"    "+money[b]["surname"]+"            "+money[b]["tr_balance"]+"                "+money[b]["currency"]["dolar"]
                    self.ui5.listWidget_2.addItem(item)
                    item = ""
                for a in money:
                    totalmoney = totalmoney + int(money[a]["tr_balance"])
            
            with open("loan.json","r") as loan:
                for a in loan.readlines():
                    self.loan = loan
                    totalloan += 1
                    self.ui5.listWidget.addItem(a)
                    

            self.ui5.totalmoney.setText(f"Total Money : {totalmoney}")
            self.ui5.totalrequest.setText(f"Total Loan Requests : {totalloan}")

            self.ui5.pushButton.clicked.connect(self.okeyLoan)

    def okeyLoan(self):
        if self.ui5.lineEdit_2.text() == "Sure":
            customer  = self.ui5.lineEdit.text()
            with open("data.json","r") as old_data:
                self.old_data = json.load(old_data)

            if customer in self.old_data:
                with open("loan.json","r") as loan:
                    loan = json.load(loan)
                    self.money = int(loan[customer])
                new_balance = int(self.old_data[customer]["tr_balance"]) + self.money 
                self.old_data[customer]["tr_balance"] = str(new_balance)

                with open("data.json","w") as new_data:
                    new_data.write(json.dumps(self.old_data))

                QtWidgets.QMessageBox.about(self,"Exit","Your order succesfully completed... \n You will exit in few seconds..")
                sys.exit()
            else:
                self.ui5.error_label.setText("Wrong id or type !")
        else:
            self.ui5.error_label.setText("Wrong id or type !")

def workIt():
    app = QtWidgets.QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec())

workIt()
