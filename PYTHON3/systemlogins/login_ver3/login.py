import os

class File:
    fileName: "none"
    path: "none"
    size: 0

    def getFilePath(self):
        print("Enter full path to database file")
        path = input(">>> ")
        print("Enter file Name")
        name = input(">>> ")
        self.path = path
        self.size = os.path.getsize(self.path)
        self.fileName = name
    def fileSearch(self, data):
        f = open(self.path, "r")
        count = 0
        output = []
        for line in f.readlines():
            line = line[0:-1]
            line = eval(line)
            for key, value in data.items():
                if value == line[key]:
                    count +=1
            if count ==len(data):
                output.append(True)
                output.append(line)
                f.close
                return output
        f.close()
        output.append(False)
        return output
    def fileWrite(self, data):
        f = open(self.path, "a")
        string = str(data)
        string += "\n"
        f.write(string)
        f.close()
        return True
fileDB = File()
class Conv:
    def controlledEval(self, string):
        if string[0]!= "o" and string[1] != 's':
            return(eval(string))
        else:
            return("Unperceived command")
    def generateData(self, rangiring):
        d1 = {}
        for i in range(0, rangiring):
            print("Input value of {}".format(system.userDataKeys[i]))
            val = input()
            d1[system.userDataKeys[i]] = val
        return d1
converter = Conv()
class System:
    name: "PythonBot"
    userDataKeys = ['login', 'password', 'name']
    systemAbyl = {"/help":"I'l write you all commands", 
            "/calk":"I'l calk for you(input expression)", 
            "/info":"I'l write all about you", 
            "/generate":"I'l generate new object(enter a name and class) [dontwork]",
            "/changeData":"I'l change or expand data about you",
            "/stop":"I'l stop"}
    def calk(self):
        print("______________________________________________")
        print("Calkulating module")
        print("Enter arithmetic expressions and get a result!")
        print("for stop enter STOP")
        print("Enter your arithmetic expression: ")
        while True:
            arithm = input()
            if arithm != "/stop":
                print(converter.controlledEval(arithm))
            else:
                break
    def fullMode(self):
        print("______________________________________________")
        print("Boot to FullControlMode")
        print("All commands are executed in the Python itself")
        print("If you want to exit out FullMode, enter /stop")
        while True:
            print("Enter command...")
            string = input(">>> ")
            if string != "/stop":
                eval(string)
    def helpp(self):
        print("______________________________________________")    
        print("Help module")
        print("Ypu can see all my abillities")
        for key, value in self.systemAbyl.items():
            print("{0}: {1}".format(key, value))    
    def info(self):
        print("______________________________________________")
        print("Info about {}".format(system.name))
        print("Name: ", system.name)
    def registrate(self):
        print("______________________________________________")
        if fileDB.size == 0:
            print("Your database file hasn't no data, so Registration Module runned")
        print("Registration")
        print("What is your login, password and name?")
        userata = converter.generateData(3)
        if fileDB.fileSearch(userdata)[0] == False:
            fileDB.fileWrite(userdata)
            userdata['logined'] = True
            return userdata
        else: 
            print("This user already exists")
            return False
    def login(self):
        print("______________________________________________")
        print("Login module")
        print("input login and password")
        userdata = converter.generateData(2)
        output = fileDB.fileSearch(userdata)
        if output[0] == True:
            userdata = output[1]
            userdata['logined'] = True
            return userdata
        else:
            print("No right login or password!")
            return False

system = System()
class User:
    name: "none"
    login: "none"
    password : "none"
    userdata = {}
    def generateUser(self, sdata):
        self.name = sdata[system.userDataKeys[2]]
        self.login = sdata[system.userDataKeys[0]]
        self.password = sdata[system.userDataKeys[1]]
        self.userdata = sdata
    def getInfoAboutUser(self):
        print("User data:     ", self.userdata)
    def changeUserData(self):
        print("______________________________________________")
        print("Chanding userdata")
        print("Are you sure that you want to change your userata?")
        inp = input(">>> ")
        if inp == "No" or inp =="no" or inp =="NO":
            print("Stopping module...")
            return False
        else:
            lineX = fileDB.fileSearch(userdata)
            d1={}
            print("Chanding data...")
            print("Enter a type of value and value itself. In end enter '/'")
            print("You can change this types: ")
            for ke in lineX[1]:
                print(ke)
            while True:
                print("Enter a type of value and value itself through ':'")
                string = input().split(':')
                if string[0] !='/':
                    d1[string[0]] = string[1]
                    userdata.update(d1)
                    user1.generateUser(userdata)
                else:
                    break
            f = open(fileDB.path, 'r')
            oldDB = f.read()
            newDB = oldDB.replace(str(lineX[1]), str(userdata))
            f.close()
            f = open(fileDB.path, 'w')
            f.write(newDB)
            return True
user1 = User
print("Python Bot")
fileDB.getFilePath()
if fileDB.size == 0:
    while True:
        userdata = system.registrate()
        if userdata['logined'] == True:
            break
else:
    print("Are you want to registrate in system?")
    inp = input(">>> ")
    if inp == "yes":
        while True:
            userdata = system.registrate()
            if userdata['logined']== True:
                userdata.pop('logined')
                break
    else:
        while True:
            userdata = system.login()
            if  userdata['logined']== True:
                userdata.pop('logined')
                break

user1.generateUser(user1, userdata)
while True:
    print("______________________________________________")
    print("What you want me to do? Enter with '/'('/help' for help with commands)")
    cmd = input()
    if cmd == "/stop":
        print("Stoping modules")
        print("______________________________________________")
        break
    elif cmd == "/help":
        system.helpp()
    elif cmd == "/changeData":
        user1.changeUserData(user1)
    elif cmd=="/botinfo":
        system.info()
    elif cmd == "/calk":
        system.calk()
    elif cmd == "/info":
        user1.getInfoAboutUser(user1)
    elif cmd == "/fullMode":
        system.fullMode()
    elif cmd=="/generate":
        print("[dontwork] command")
    else:
        print("Error: Undefined command")
