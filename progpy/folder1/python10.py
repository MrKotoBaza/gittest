import tkinter as tk
from tkinter import filedialog as fg
import hashlib
import uuid
import os
fileDB = ""
userdata = {}

def fileWrite(path, data):
    data = str(data)+ "\n"
    f = open(path, 'r')
    oldData = f.read()
    f.close()
    newData = oldData+data
    f= open(path, "w")
    f.write(newData)
def getfile():
    global fileDB
    fileDB = fg.askopenfilename()
def hashData(text1):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text1.encode()).hexdigest() + ':' + salt
def reHashData(text1, text2):
    password, salt = text2.split(':')
    return password == hashlib.sha256(salt.encode() + text1.encode()).hexdigest()
def destroyWin():
    root.destroy()
    if 'win1' in globals():
        win1.destroy()
def fileReadTF(path, data):
    file = open(path, "r")
    count = 0
    for line in file.readlines():
        line = eval(line)
        for key, value in data.items():
            if key != "password":
                if value != line[key]:
                    count += 1
            else:
                if reHashData(data['password'], line['password'])==False:
                    count+=1
        if count == 0:
            return True
    file.close()
    return False
def logining():
    global userdata
    global fileDB
    if fileDB =="":
        print("Need filepath")
    elif login.get() == "" or passw.get() == "":
        print("Need data in entries")
    else:
        userdata['login'] = login.get()
        userdata['password'] = passw.get()
        if fileReadTF(fileDB, userdata):
            destroyWin()
            createMineWindow()
        else:
            print("Go relogin, no right data")
            print(userdata)
def registrate():
    global win1
    global userdata
    global fileDB
    global name1
    global login1
    global passw1
    win1 = tk.Toplevel(root)

    lbl4 = tk.Label(win1, text="Регистрация")
    lbl5 = tk.Label(win1, text = "Имя")
    lbl6 = tk.Label(win1, text = "Логин")
    lbl7 = tk.Label(win1, text = "Пароль")

    name1 = tk.Entry(win1)
    login1 = tk.Entry(win1)
    passw1 = tk.Entry(win1)

    btn1 = tk.Button(win1, text="Зарегистрироваться", command= endRegistrate)
    btn2 = tk.Button(win1, text="Выйти", command = destroyWin)
    btn3 = tk.Button(win1, text="Выбрать путь для файла", command= getfile)

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
            fileWrite(fileDB, userdata)
            destroyWin()
    else:
        print("Need filepath")



root = tk.Tk()
root.title("Вход")
lbl0 = tk.Label(root, text = "Вход в систему")
lbl0.grid(row =0, column = 0, columnspan = 4)
lbl1 = tk.Label(root, text = "Логин")
lbl1.grid(row = 1, column = 0, columnspan = 2)
lbl2 = tk.Label(root, text = "Пароль")
lbl2.grid(row = 2, column = 0, columnspan = 2)
login = tk.Entry(root)
login.grid(row = 1, column = 2, columnspan = 2)
passw = tk.Entry(root)
passw.grid(row = 2, column = 2, columnspan = 2)
btn1 = tk.Button(root, text = 'Войти', command = logining)
btn2 = tk.Button(root, text = 'Выбрать расположение файла', command= getfile)
btn3 = tk.Button(root, text = 'Закрыть', command = destroyWin)
btn4 = tk.Button(root, text = 'Регистрация', command = registrate)
btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)
btn4.grid(row = 3, column = 3)
root.mainloop()