import tkinter as tk
from tkinter import filedialog as fg
import hashlib
import uuid

fileDB = ""
userdata = {}
root = tk.Tk()

def getfile():
    global fileDB
    fileDB = fg.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

def fileWrite(path, data):
    with open (path, 'r') as f:
        old_data = f.read()
        dataRe = dataRedo(data, 'logining')
        foundSTR = fileLogin(path, dataRe)[1]

        new_data = old_data.replace(str(foundSTR), str(data))

    with open (path, 'w') as f:
        f.write(new_data)

def dataRedo(data, out):
    reData = {}
    if out == "registrate":
        reData['registrate'] = 'True'
        reData.update(data)
    if out == "logining":    
        reData['login'] = data['login']
        reData['password'] = data['password']
        reData['logined'] = True
    return reData

def hashData(text1):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text1.encode()).hexdigest() + ':' + salt

def reHashData(text1, text2):
    password, salt = text2.split(':')
    return password == hashlib.sha256(salt.encode() + text1.encode()).hexdigest()


def fileLogin(path, data):
    #импорт data в приведенном виде
    f = open(path, "r")
    count = 0
    result = []
    for line in f.readlines():
        line = eval(line)
        if 'logined' in data.keys():
            if data['login'] != line['login']:
                count+=1
        elif 'registrate' in data.keys():
            result.append(False)
            result.append(data)
        else:
            for key, value in data.items():
                if key != "password":
                    if value != line[key]:
                        count += 1
                else:
                    if reHashData(data['password'], line['password'])==False:
                        count+=1
        if count == 0:
            result.append(True)
            result.append(line)
            f.close()
            return result
    f.close()
    result.append(False)
    return result

def createLoginWindow():
    global userdata
    global fileDB
    global root
    global loginWin
    global login
    global passw
    loginWin = tk.Toplevel(root)
    loginWin.title("Вход")
    lbl0 = tk.Label(loginWin, text = "Вход в систему")
    lbl0.grid(row =0, column = 0, columnspan = 4)
    lbl1 = tk.Label(loginWin, text = "Логин")
    lbl1.grid(row = 1, column = 0, columnspan = 2)
    lbl2 = tk.Label(loginWin, text = "Пароль")
    lbl2.grid(row = 2, column = 0, columnspan = 2)
    login = tk.Entry(loginWin)
    login.grid(row = 1, column = 2, columnspan = 2)
    passw = tk.Entry(loginWin)
    passw.grid(row = 2, column = 2, columnspan = 2)
    btn1 = tk.Button(loginWin, text = 'Войти', command = logining)
    btn2 = tk.Button(loginWin, text = 'Выбрать расположение файла', command= getfile)
    btn3 = tk.Button(loginWin, text = 'Закрыть', command = destroyWins)
    btn4 = tk.Button(loginWin, text = 'Регистрация', command = createRegistrateWindow)
    btn1.grid(row = 3, column = 0)
    btn2.grid(row = 3, column = 1)
    btn3.grid(row = 3, column = 2)
    btn4.grid(row = 3, column = 3)
    login.focus()

def createRegistrateWindow():
    global userdata
    global fileDB
    global registrateWin
    global root
    global name1
    global login1
    global passw1
    registrateWin = tk.Toplevel(root)

    lbl4 = tk.Label(registrateWin, text="Регистрация")
    lbl5 = tk.Label(registrateWin, text = "Имя")
    lbl6 = tk.Label(registrateWin, text = "Логин")
    lbl7 = tk.Label(registrateWin, text = "Пароль")

    name1 = tk.Entry(registrateWin)
    login1 = tk.Entry(registrateWin)
    passw1 = tk.Entry(registrateWin)

    btn1 = tk.Button(registrateWin, text="Зарегистрироваться", command= endRegistrate)
    btn2 = tk.Button(registrateWin, text="Выйти", command = destroyWins)
    btn3 = tk.Button(registrateWin, text="Выбрать путь для файла", command= getfile)

    lbl4.grid(row = 0, column = 0, columnspan = 2)
    lbl5.grid(row = 1, column = 0)
    lbl6.grid(row = 2, column = 0)
    lbl7.grid(row = 3, column = 0)
    name1.grid(row = 1, column = 1)
    login1.grid(row = 2, column = 1)
    passw1.grid(row = 3, column = 1)
    btn1.grid(row = 4, column = 0)
    btn2.grid(row = 4, column = 1)
    btn3.grid(row = 5, column = 0)

    name1.focus()

def endRegistrate():
    global userdata
    global fileDB
    global name1
    global login1
    global passw1
    if fileDB != "":
        if name1.get() =="" or login1.get() =="" or passw1.get()==""    :
            print("Need more data")
        else:
            userdata['name'] = name1.get()
            userdata['login'] = login1.get()
            x1 = passw1.get()
            userdata['password'] = hashData(x1)
            chData = {}
            chData['notlogined'] = True
            chData['login'] = userdata['login']
            chData['password'] = x1

            if fileLogin(fileDB, chData)[0]==False:
                fileWrite(fileDB, userdata)
                destroyWins()
    else:
        print("Need filepath")

def destroyWins():
    if 'registrateWin' in globals():
        registrateWin.destroy()
    if 'loginWin' in globals():
        loginWin.destroy()
    if "changeWin" in globals():
        changeWin.destroy()

def destroyP():
    destroyWins()
    root.destroy()

def logining():
    global userdata
    global fileDB
    global login
    global passw
    if fileDB =="":
        print("Need filepath")
    elif login.get() == "" or passw.get() == "":
        print("Need data in entries")
    else:
        userdata['login'] = login.get()
        userdata['password'] = passw.get()
        logs =fileLogin(fileDB, userdata)
        if logs[0]:
            userdata = logs[1]
            destroyWins()
            logined()

        else:
            print("Go relogin, no right data")
            print(userdata)

def calk():
    global root
    calkWin = tk.Toplevel(root)
    entry = tk.Entry(calkWin)
    btn1 = tk.Button(calkWin, text = "1", command = appendChar)
    btn2 = tk.Button(calkWin, text = "2", command = appendChar)
    btn3 = tk.Button(calkWin, text = "3", command = appendChar)
    btn4 = tk.Button(calkWin, text = "4", command = appendChar)
    btn5 = tk.Button(calkWin, text = "5", command = appendChar)
    btn6 = tk.Button(calkWin, text = "6", command = appendChar)
    btn7 = tk.Button(calkWin, text = "7", command = appendChar)
    btn8 = tk.Button(calkWin, text = "8", command = appendChar)
    btn9 = tk.Button(calkWin, text = "9", command = appendChar)
    btnX = tk.Button(calkWin, text = "<", command = appendChar) #delLastChar
    btn0 = tk.Button(calkWin, text = "0", command = appendChar)
    btnZ = tk.Button(calkWin, text = "=", command = appendChar) #calkculateEntry
    entry.grid(row = 0, column = 0, columnspan = 3)
    btn1.grid(row = 1, column = 0)
    btn2.grid(row = 1, column = 1)
    btn3.grid(row = 1, column = 2)
    btn4.grid(row = 2, column = 0)
    btn5.grid(row = 2, column = 1)
    btn6.grid(row = 2, column = 2)
    btn7.grid(row = 3, column = 0)
    btn8.grid(row = 3, column = 1)
    btn9.grid(row = 3, column = 2)
    btnX.grid(row = 4, column = 0)
    btn0.grid(row = 4, column = 1)
    btnZ.grid(row = 4, column = 2)

def appendChar():
    print("char")

def createChangeDataWindow():
    global root
    global changeWin
    global userdata
    global fileDB
    global entryData
    global entryBaseData
    changeWin = tk.Toplevel()
    lbl1 = tk.Label(changeWin, text="Это окно смены \nданных о пользователе")
    lbl2 = tk.Label(changeWin, text="Пропишите тип данных и сами данные черех двоеточие") 
    entryData = tk.Entry(changeWin)
    lbl3 = tk.Label(changeWin, text="Для смены имени, логина и пароля, пропишите name,\n login или password и само значение")
    entryBaseData = tk.Entry(changeWin)
    lbl4 = tk.Label(changeWin, text="Для изменения данных, нажмите на кнопку")
    button = tk.Button(changeWin, text="Change", command = changeData)
    lbl5 = tk.Label(changeWin, text="Или же завершите изменение")
    btn1 = tk.Button(changeWin, text="Выйти", command= destroyWins)

    lbl1.grid(row = 0, column = 0, columnspan = 2)
    lbl2.grid(row = 1, column = 0)
    entryData.grid(row = 1, column = 1)
    lbl3.grid(row =2, column = 0)
    entryBaseData.grid(row = 2, column = 1)
    lbl4.grid(row = 3, column = 0)
    button.grid(row = 3, column = 1)
    lbl5.grid(row = 4, column = 0)
    btn1.grid(row = 4, column = 1)

def changeData():
    global userdata
    global fileDB
    global entryData
    global entryBaseData

    if entryData.get() == "" and entryBaseData.get() == "":
        print("Need entries")
    elif entryData.get() == "":
        if entryBaseData.get().split(":")[0] == "password":
            ans = input("Are you sure?")
            if ans == "YES":
                userdata["password"] = entryBaseData.get().split(":")[1]
                fileWrite(fileDB, userdata)
                entryBaseData.delete(0, "end")
                print("Changed")
                print(userdata)
            else:
                print("Not confirmed")
        else:
            ans = input("Are you sure?")
            if ans == "YES":
                userdata[entryBaseData.get().split(":")[0]] = entryBaseData.get().split(":")[1]
                fileWrite(fileDB, userdata)
                entryBaseData.delete(0, "end")
                print("Changed")
                print(userdata)
            else:
                print("Not confirmed")
    elif entryBaseData.get() == "":
        data = entryData.get().split(":")
        dataDict = {data[0]:data[1]}
        userdata.update(dataDict)
        print("Changed")
        print(userdata)
        fileWrite(fileDB, userdata)
        entryData.delete(0, "end")
    else:
        print("Too much data")







root.title("Основное окно")
lbl1 = tk.Label(root, text="Основное окно программы, все модули открываются в других окнах")
lbl1.grid(row = 0, column = 0, columnspan = 2)
btn1 = tk.Button(root, text="Войти", command = createLoginWindow)
btn1.grid(row = 1, column = 0, columnspan = 2)

def logined():
    global btn1
    print("It's ok")
    lbl2 = tk.Label(root, text="Это окно позволяет открыть\nдругие окна, в кльлоых будут\nработать другие модули")
    lbl2.grid(row = 1, column = 0, rowspan = 2)
    btn1.configure(text = "Калькулятор", command = calk)
    btn1.grid(row =2, column = 1)
    btn2 = tk.Button(root, text="Изменить данные", command = createChangeDataWindow)
    btn2.grid(row = 3, column = 1)
    btnlast = tk.Button(root, text="Выйти из программы", command = destroyP)
    btnlast.grid(row = 4, column = 1)

root.mainloop()