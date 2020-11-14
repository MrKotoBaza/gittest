import os


class Person:
    name = "none"
    login = "none"
    password = "none"

    def generatePerson(self, data):
        self.name = data[0]
        self.login = data[1]
        self.password = data[2]

    def getInfoAboutUser(self):
        print("User name:     ", self.name)
        print("User login:    ", self.login)
        print("User password: ", self.password)


class File:
    name: "none"
    location: "none"

    def fileSize(self, location):
        return os.path.getsize(self.location)

    def generateFile(self, location, name):
        self.name = name
        self.location = location

    def fileReadTF(self, data):  # fileRead True or False
        f = open(self.location, "r")
        i = len(data)
        lineX = ""
        for i in data:
            lineX += "{}:".format(i)
        lineX += "\n"
        for line in f.readlines():
            if line == lineX:
                f.close()
                return True
        f.close()
        return False

    def fileWrite(self, data):
        f = open(self.location, "a")
        i = len(data)
        line = ""
        for i in data:
            line += "{}:".format(i)
        line += "\n"
        f.write(line)
        f.close()


user1 = Person()
database = File()
database.generateFile("login_ver1\\sss.txt", "database")

abillities = {"/help": "i'l write you all commands",
              "/calk": "I'l calk for you(input expression)",
              "/info": "I'l write all about you",
              "/generate": "I'l generate new object(enter a name and class)"}


def help():
    print("It's a help module. Here you can see all my abillities:")
    for key, value in abillities.items():
        print("{0}: {1}".format(key, value))


def logining():
    if database.fileSize(database.location) == 0:
        print("i have no accounts")
        print("Registartion!")
        print("What is your name, login and password?")
        name = input()
        login = input()
        password = input()
        userdata = []
        userdata.append(name)
        userdata.append(login)
        userdata.append(password)
        user1.generatePerson(userdata)
        database.fileWrite(userdata)
        return True
    else:
        print("I need to understand who you are")
        print("Has you an account?")
        inf = input()
        if inf == "No" or inf == "no" or inf == "NO":
            print("Registartion!")
            print("What is your name, login and password?")
            name = input()
            login = input()
            password = input()
            userdata = []
            userdata.append(name)
            userdata.append(login)
            userdata.append(password)
            inf2 = database.fileReadTF(userdata)
            if inf2 == False:
                user1.generatePerson(userdata)
                database.fileWrite(userdata)
                return True
            else:
                print("This user already exists")
                return False
        elif inf == "Yes" or inf == "yes" or inf == "YES":
            print("Logining!")
            print("input name, login, password")
            name = input()
            login = input()
            password = input()
            userdata = []
            userdata.append(name)
            userdata.append(login)
            userdata.append(password)
            inf2 = database.fileReadTF(userdata)
            if inf2 == True:
                user1.generatePerson(userdata)
                return True
            else:
                print("No right name, login or password!")
                return False
        else:
            print("Error: Undefined command")
            return False


print("Logining module!")
while True:
    temp = True
    if temp == True:
        break
print(" ")
print("Ready!")
print(" ")
while True:
    print("What you want me to do? Enter with /")
    cmd = input()
    if cmd == "/help":
        help()
    elif cmd == "/stop":
        print("Stoping modules")
        break
    elif cmd == "/fullcontrol":
        inp = input()
        eval(inp)
    else:
        print("Error: Undefined command")
