import json
import hashlib

class User(object):
    name: ""
    rules: ""
    password: ""
    data = {}

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.data.update({"name": name})
        self.data.update({"password": password})

    def setRules(self, rulesName):
        self.rules = rulesName
        self.data.update({"rules": rulesName})

    def getName(self):
        return self.name

    def getRules(self):
        return self.rules

    def changePassword(self, password):
        self.password = password

def encryptPassw(word):
    h = hashlib.md5(word.encode("utf-8"))
    return h.hexdigest()

def decryptPassw(word, mask):
    if hashlib.md5(word.encode("utf-8")).hexdigest() == mask:
        return True

def writeData():
    with open("data.txt", "rw") as dataFile:
        dataFile.write(str(user.data) + "\n")

def registration():
    global user
    print("Hello! It's PythonBot")
    print("You haven't registrate, you must be registrate, because enter your name and password")
    name = input("Enter name: ")
    password = input("Enter password: ")
    password2 = input("Enter password twice: ")

    if password == password2:
        enc = encryptPassw(password)
        user = User(name, enc)
        user.setRules("ADMIN")

        writeData()

registration()
    
