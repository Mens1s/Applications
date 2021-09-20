import json 
def login(user,password):
    with open("data.json","r") as data:
        data = json.load(data)
        if user in data:
            if password == data[user]["password"]:
                return 1,data[user]["name"],data[user]["surname"],data[user]["tr_balance"],data[user]["currency"]
            else:
                return 0
        else:
            return 0
def controlUser(user):
    with open("data.json","r") as data:
        data = json.load(data)
        if user in data:
            return 1
