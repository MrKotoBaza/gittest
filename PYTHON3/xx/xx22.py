from tkinter import *
tk = Tk()
tk.geometry("440x170")
tk.resizable(False, False)


def button_pressing1():
    pass
def button_pressing2():
    pass
def button_pressing3():
    pass

b1 = Button(tk, text = "Command1", command = button_pressing1, font = ("Times New Roman", 15))

b2 = Button(tk, text = "Command2", command = button_pressing2, font = ("Times New Roman", 15))

b3 = Button(tk, text = "Command3", command = button_pressing3, font = ("Times New Roman", 15))

b1.place(x = 10, y = 100, width = 120, height = 50)
b2.place(x = 150, y = 100, width = 120, height = 50)
b3.place(x = 300, y = 100, width = 120, height = 50)

lbl1 = Label(tk, text="Started", font = ("Times New Roman", 21, "bold"))
lbl1.place(x = 250, y = 25, width = 300, height = 50)

tk.mainloop()