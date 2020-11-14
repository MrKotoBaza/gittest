import os
import hashlib

fileDB = []
userdata = {}
userDataKeys = ['login', 'password', 'name']
abillities = {
    "/help": "I'l write you all commands",
    "/calk": "I'l calk for you(input expression)",
    "/info": "I'l write all about you",
    "/generate": "I'l generate new object(enter a name and class) [dontwork]",
    "/changeData": "I'l change or expand data about you",
    "/stop": "I'l stop"}


def getFile():
    data = []
    global fileDB
    global savedLastFilePath
    if os.path.isfile(savedLastFilePath) == False:
        print("Enter full path to database file or to folder for new database file")
        print("Please, enter right path, else i will need to fullreload")
        path = input(">>> ")
        if path == "":
            print("Not a path")
            return False
        else:
            if os.path.isfile(path) == True:
                if path.find('.txt') != -1:
                    print("It's a right path to file")
                    data.append(path)
                    data.append(os.path.split(path)[1])
                    data.append(os.path.getsize(path))
                    data.append(os.path.dirname(path))
                    print("File ready to work>>>")
                else:
                    print("Wrong path")
                    return False

            else:
                print("it's a folder, getting logining file")
                path += r"\login.txt"
                f = open(path, 'a')
                f.close()
                data.append(path)
                data.append(os.path.split(path)[1])
                data.append(os.path.getsize(path))
                data.append(os.path.dirname(path))
                print("File ready to wotk>>>")
        fileDB = data
        savedLastFilePath = data[0]
    else:
        path = savedLastFilePath
        data.append(path)
        data.append(os.path.split(path)[1])
        data.append(os.path.getsize(path))
        data.append(os.path.dirname(path))
        print("File ready to wotk>>>")
        fileDB = data
    return True


def hashing(string):
    hash = hashlib.sha256(bytes(string, encoding="utf-8"))
    return hash.hexdigest()


def generateData(rangiring):
    d1 = {}
    for i in range(0, rangiring):
        print("Input value of {}".format(userDataKeys[i]))
        val = input()
        if userDataKeys[i] == "password":
            val = hashing(val)
        d1[userDataKeys[i]] = val
    return d1


def fileSearch(data, filePath):
    f = open(filePath, "r")
    count = 0
    output = []
    if type(data) == dict:
        for line in f.readlines():
            line = line[0:-1]
            line = eval(line)
            for key, value in data.items():
                if value == line[key]:
                    count += 1
            if count == len(data):
                output.append(True)
                output.append(line)
                f.close
                return output
    f.close()
    output.append(False)
    return output


def fileWrite(data, filePath):
    f = open(filePath, "a")
    string = str(data)
    string += "\n"
    f.write(string)
    f.close()
    return True


def chanding():
    lineX = fileSearch(userdata, fileDB[0])
    d1 = {}
    print("Chanding data...")
    print("Enter a type of value and value itself. In end enter '/stop'")
    print("You can change this types: ")
    for key, val in lineX[1].items():
        if key != 'password':
            print("{0} : {1}".format(key, val))
        else:
            print(key)
    while True:
        print("Enter a type of value and value itself through ':'")
        string = input().split(':')
        if string[0] != '/stop':
            if string[0] == "password":
                string[1] = hashing(string[1])
            d1[string[0]] = string[1]
            userdata.update(d1)
        else:
            break
    f = open(fileDB[0], 'r')
    oldDB = f.read()
    newDB = oldDB.replace(str(lineX[1]), str(userdata))
    f.close()
    f = open(fileDB[0], 'w')
    f.write(newDB)
    return True


def registrate():
    if fileDB[2] == 0:
        print("Your database file has no data, so Registration Module runned")
    print("Registration")
    print("What is your login, password and name?")
    userdata = generateData(3)
    if fileSearch(userdata, fileDB[0])[0] == False:
        fileWrite(userdata, fileDB[0])
        userdata['logined'] = True
        return userdata
    else:
        print("This user already exists")
        userdata = {'logined': False}


def login():
    print("Logining")
    print("input login and password")
    userdata = generateData(2)
    output = fileSearch(userdata, fileDB[0])
    if output[0] == True:
        userdata = output[1]
        userdata['logined'] = True
        return userdata
    else:
        print("No right login or password!")
        userdata = {'logined': False}
        return userdata


def controlledEval(string):
    if string[0] != "o" and string[1] != 's':
        result = eval(string)
        logSave(string, result)
        return result

    else:
        return("Unperceived command")


def changeData():
    print("Chanding data module")
    print("You can change data of your account or expand data. Do you want change data? 'yes'")
    ans = input()
    if ans == 'yes':
        if chanding() != True:
            print("What's happend...")
    else:
        print("Cannot understand")


def helpp():
    print("Here you can see all my abillities:")
    for key, value in abillities.items():
        print("{0}: {1}".format(key, value))


def info():
    print("Output info about you")
    for key, value in userdata.items():
        if key != 'password':
            print("{0}: {1}".format(key, value))
        else:
            print(key)


def calk():
    print("Calkulating module")
    print("Enter arithmetic expressions and get a result!")
    print("for stop enter /stop")
    while True:
        try:
            print("Enter your arithmetic expression: ")
            arithm = input()
            if arithm != "/stop":
                print(controlledEval(arithm))
            else:
                break
        except ZeroDivisionError:
            print("division by zero")
        except ValueError:
            print("wrong value")


def fullMode():
    print("It's dangerous!")
    print("Boot to FullControlMode")
    print("All commands are executed in the Python itself")
    print("If you want to exit out FullMode, enter /stop")
    while True:
        try:
            print("Enter command...")
            string = input(">>> ")
            if string != "/stop":
                result = eval(string)
                logSave(string, result)
            else:
                break
        except SyntaxError:
            print("Wrong syntax")
        except ValueError:
            print("Wrong value")


def logining():
    global userdata
    if fileDB[2] == 0:
        while True:
            userdata = registrate()
            if userdata['logined'] == True:
                userdata.pop('logined')
                break
    else:
        print("Are you want to registrate in system? If yes, enter 'yes'")
        inp = input(">>> ")
        if inp == "yes":
            while True:
                userdata = registrate()
                if userdata['logined'] == True:
                    userdata.pop('logined')
                    break
        else:
            while True:
                userdata = login()
                if userdata['logined'] == True:
                    userdata.pop('logined')
                    break
                else:
                    logining()
                    break


def botinfo():
    print("Do you want to know a little about me?")
    print("")
    print("I work with this database file: ", fileDB[0])
    print("This file takes {} bytes".format(fileDB[2]))
    print("To learn more about my abillities, enter '/help'")
    print("I can go to fullMode, there Python can execute your commands independently. Enter '/fullMode'")
    print("")
    print("WARNING!!! It's dangerous!")


def logSave(string, result):
    note = []
    note.append(userdata['name'])
    note.append(userdata['login'])
    note.append(string)
    note.append(str(result))
    fileWrite(note, fileDB[3]+r"\logs.txt")


print("Hello, I'm PythonBot!")
print("To login to me, enter the path of file with logins")
while True:
    if getFile() == True:
        break
    else:
        getFile()
print("Running LoginModule")
logining()
print("You are logined to me!")
while True:
    print("What you want me to do? Enter with '/'('/help' for help with comands)")
    cmd = input()
    if cmd == "/help":
        helpp()
    elif cmd == "/changeData":
        changeData()
    elif cmd == "/info":
        info()
    elif cmd == "/botinfo":
        botinfo()
    elif cmd == "/stop":
        print("Stoping modules")
        print("______________________________________________")
        break
    elif cmd == "/calk":
        calk()
    elif cmd == "/fullMode":
        print("")
        print("WARNING!!!")
        fullMode()
        break
    elif cmd == "/generate":
        print("[dontwork] command")
    else:
        print("Error: Undefined command")


# Идеи по развитию бота:
# 1. Обратныый переход на ООП для более красивого использования fullmode и eval [в долгий ящик]
# 2. Дополнительные украшательства кода и интерфейса(например, перестройка всех функций под декораторы) + добавление GUI
# 3. Перестройка датабазы и логов под ведение JSON
# 4. Доведение проверки ввода через try/except
# 5. Логопарсинг
# 6. Добавление к логам time
# 7. Смена языка [в долгий ящик]
# 8. Добавление задержки выполнения некоторых комманд
# 9. Создание новых переменных под видом элементов. Создание элементного окружения и взаимодейтвия этих элементов [вопрос с реализацией]
# 10. Полный переход на аккаунтную систему [вопрос с реализацией]
# 11. Взаимодействие с браузером. Создание системы "сервер" - "клиент" через OpenServer, взаимодействие с HTML, CSS, JS(част развития от JSON) [в долгий ящик]
# 12. Оптимизация бота
# 13. Управление любыми типами файлов, увеличение возможностей логопарсинга до взаимодействия с группами файлов [в долгий ящик]
# 15. Абсолютный поиск через FileSearch
