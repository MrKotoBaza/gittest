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

def hashData(text1):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text1.encode()).hexdigest() + ':' + salt

def reHashData(text1, text2):
    password, salt = text2.split(':')
    return password == hashlib.sha256(salt.encode() + text1.encode()).hexdigest()

def fileWrite(path, data, foundSTR):
    with open (path, 'r') as f:
        old_data = f.read()
        data.pop('logined', None)
        new_data = old_data.replace(str(foundSTR), str(data))

    with open (path, 'w') as f:
        f.write(new_data)

def fileRead(path, data):
    #импорт data в приведенном виде

    f = open(path, "r")
    count = 0
    result = []
    for line in f.readlines():
        line = eval(line)
        if 'logined' in data.keys():
            for key, value in data.items():
                if value != line[key]:
                    count += 1
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
            check = fileRead(fileDB, configurateData("reg", userdata))
            if check[0]==False:
                fileWrite(fileDB, userdata, "")
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
        x1 = passw1.get()
        userdata['password'] = hashData(x1)
        logs =fileLogin(fileDB, userdata)
        if logs[0]:
            userdata = logs[1]
            destroyWins()
            logined()

        else:
            print("Go relogin, no right data")
            print(userdata)



