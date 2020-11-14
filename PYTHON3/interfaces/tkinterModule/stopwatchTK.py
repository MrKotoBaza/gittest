import tkinter as tk
from datetime import datetime
temp = 0
afterID = ""
def startSW():
    btn1.grid_forget()
    btn2.grid(row = 1, column = 0, columnspan = 2)
    tick()

def tick():
    global temp, afterID
    afterID = window.after(1000, tick)
    temp +=1
    ftemp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=ftemp)

def stopSW():
    btn2.grid_forget()
    btn3.grid(row = 1, column = 0)
    btn4.grid(row = 1, column =1)
    window.after_cancel(afterID)

def continueSW():
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row = 1, column = 0, columnspan = 2)

def resetSW():
    global temp
    temp = 0
    label1.configure(text = "00:00")
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row =1, column = 0, columnspan = 2)

window = tk.Tk()

label1 = tk.Label(window, text="00:00", font=("Ubuntu, 100"), width = 5)
label1.grid(row =0, column = 0, columnspan = 2)

btn1 = tk.Button(window, text = "Start", font =("Ubuntu", 30), command = startSW)
btn2 = tk.Button(window, text = "Stop", font =("Ubuntu", 30), command = stopSW)
btn3 = tk.Button(window, text = "Continue", font =("Ubuntu", 30), command = continueSW)
btn4 = tk.Button(window, text = "Reset", font =("Ubuntu", 30), command = resetSW)

btn1.grid(row =1, column = 0, columnspan = 2)

window.mainloop()


 
