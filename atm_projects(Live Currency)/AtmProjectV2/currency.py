import requests
rates = requests.get("https://v1.nocodeapi.com/test123213/cx/ERFlVAPtciohTySe/rates").json()

class Currency:
    def getAll():
        return rates["rates"]

    def getCurrency(target):
        return rates["rates"][target]
