import time
import requests
class getCurrency():
    def __init__(self,curr):
        self.curr=curr
    def currency(self):
        return requests.get("https://v1.nocodeapi.com/test123213/cx/ERFlVAPtciohTySe/rates").json()
users={
    "1":{
        "name":"Ahmet",
        "surname":"Yigit",
        "balance":15000,
        "password":1
    },
    "2":{
        "name":"Ahmet",
        "surname":"Yigit",
        "balance":15000,
        "password":101010
    }
}
class Sign_up():
    def __init__(self,tc,name,surname,password):
        self.tc = tc
        self.name = name
        self.surname=surname
        self.password=password
    def kaydol(self):
        if(self.tc not in users):
            new_user={
                "name":self.name,
                "surname":self.surname,
                "balance":0,
                "password":self.password
            }
            users[self.tc]=new_user
            return True
        else:
            return False    
class Login():
    def __init__(self,tc,password):
        self.tc = tc
        self.password = password
    def login(self):
        if self.tc in users:
            if users[self.tc]["password"]==self.password:
                return 1
            else:
                return 0    
while True:
    print("""
    Good morning!
    Please select your transaction
    1-) Sign-Up
    2-) Log-in
    3-) deposit with TC
    4-) withdraw with TC
    """)   
    choice =int(input())
    if choice == 1:
        tc = input("Enter Your TC   :")
        name = input("Please enter your Name    :")
        surname = input("Please Enter Your Surname  :")
        password = input("Please enter your Password    :")
        returned = Sign_up(tc,name,surname,password).kaydol()
        if returned==True:
            print("You have registered succesfully, You are being redirected to the homepage!")
            time.sleep(3)
            break
        else:
            print("Your TC is already using. Please contact us!")
            time.sleep(3)
            break
    elif choice==2:
        tc = input("Enter Your TC   :")
        password = int(input("Please enter your Password    :"))
        returned=Login(tc,password).login()
        print(returned)
        if returned==1:
            print("You are succesfuly loged in!")
            while True:
                print("Please Select your transaction")
                print("""
                1-)Show balance
                2-)withdraw 
                3-)deposit
                4-)Transfer/EFT 
                5-)take a foreign currency
                """)
                new_c= int(input())
                if new_c==1:
                    print("Your balance is {}".format(users[tc]["balance"]))
                    print("Do you have a currency? if your answer is yes  enter 1!")
                    choice_1= input()
                    if choice_1=="1":
                        print("what is your currecy please type! like TRY")
                        searc= input()
                        print("Your currency balance is {}".format(users[tc]["balance"+searc]))
                elif new_c==2:
                    print("Please enter your amount of money")
                    money = int(input())
                    control = users[tc]["balance"] - money
                    if control >= 0:
                        users[tc]["balance"] = control
                        print("Your new balance is {}".format(users[tc]["balance"]))
                    else:
                        print("You don't have enough money! \n Your balance is {}".format(users[tc]["balance"]))  
                    time.sleep(2) 
                elif new_c==3:
                    print("Please enter your amount of money")
                    money = int(input())
                    users[tc]["balance"] += money
                    print("Your new balance is {}".format(users[tc]["balance"]))
                    time.sleep(2)
                elif new_c==4:
                    print("Please enter receiver's TC ")
                    new_tc=  input()
                    if new_tc not in users:
                        print("Wrong TC!")
                    else:   
                        print("Please enter your amount of money")
                        money = int(input())
                        users[new_tc]["balance"] += money
                        print("EFT/Transfer has done succesfully")
                elif new_c==5:
                    print("Please enter your currency! like TRY")
                    cur= input()
                    returned=getCurrency(cur).currency()
                    reel_cur = returned["rates"][cur]
                    print("1$ is equal {} {}".format(reel_cur,cur))
                    print("Do you want to buy? If your answer is yes enter 1 !")
                    choice_two=int(input())
                    if choice_two==1:
                        print("How much do you want to buy {}".format(cur))
                        curency = int(input())
                        if curency <= users[tc]["balance"]:
                            print("You have bought {} {}".format(reel_cur*curency,cur))
                            users[tc]["balance"] -= curency
                            users[tc]["balance"+cur]=reel_cur*curency
                        time.sleep(2)
                        
                    else:
                        print("You are being redirected to the homepage!")
                        time.sleep(2)
                        break
                else:
                    print("Wrong number!")
        else:
            print("wrong tc/password")        
    elif choice==3:
        print("Please enter your TC ! ")
        tc=input()
        if tc in users:
            print("Please enter your amount of money")
            money = int(input())
            users[tc]["balance"] += money
            print("Your new balance is {}".format(users[tc]["balance"]))
            time.sleep(2)
        else:
            print("You are entered wrong TC!")
            time.sleep(2)    
    elif choice==4:
        print("Please enter your TC ! ")
        tc=input()
        if tc in users:
            print("Please enter your amount of money")
            money = int(input())
            control = users[tc]["balance"] - money
            if control >= 0:
                users[tc]["balance"] = control
                print("Your new balance is {}".format(users[tc]["balance"]))
            else:
                print("You don't have enough money! \n Your balance is {}".format(users[tc]["balance"]))  
            time.sleep(2)       
        else:
            print("You are entered wrong TC!")
            time.sleep(2)           
