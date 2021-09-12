import json 
def login(user,password):
    with open("data.json","r") as data:
        data = json.load(data)
        if user in data:
            if password == data[user]["password"]:
                return 1,data["name"],data["surname"],data["tr_balance"],data["usd_balance"]
            else:
                return 0
        else:
            return 0
