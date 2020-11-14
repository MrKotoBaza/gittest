from tkinter import *
 
signs = {1:'+', 2:'-', 3:'*', 4:'/'}
 
class Calculator:
    def __init__(self, master):
        self.e1 = Entry(master, width=40)
        self.e2 = Entry(master, width=40)
        self.l = Label(master, bg='black', fg='white', width=40)
        self.e1.pack()
        self.e2.pack()
        self.l.pack()
        for i in signs:
            self.name = 'b' + str(i)
            self.name = Button(master, text=signs[i])
            self.name['command'] = self.numer(signs[i])
            self.name.pack()
    def numer(self, sign):
        try:
            self.l['text'] = str(eval(self.e1.get() + sign + self.e2.get()))
        except:
            self.l['text'] = 'Error'
 
root = Tk()
calc1 = Calculator(root)
root.mainloop()