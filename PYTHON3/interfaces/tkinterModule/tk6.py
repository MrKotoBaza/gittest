from tkinter import *
from tkinter.messagebox import *

def asc1(event):
    answer = askquestion("Asc question", "Q 1")
    lbl1.configure(text=answer)

def asc2(event):
    answer = askokcancel("Asc question", "Q 2")
    lbl2.configure(text=answer)

def asc3(event):
    answer = askyesno("Asc question", "Q 3")
    lbl3.configure(text=answer)

def asc4(event):
    answer = askretrycancel("Asc question", "Q 4")
    lbl4.configure(text=answer)
root = Tk()

btn1 = Button(root, text = "BTN1", width = 12)
btn1.grid(row = 0, column = 0, sticky = "ew")
lbl1 = Label(root, width = 12)
lbl1.grid(row = 0, column = 1)

btn2 = Button(root, text = "BTN2", width = 12)
btn2.grid(row = 1, column = 0, sticky = "ew")
lbl2 = Label(root, width = 12)
lbl2.grid(row = 1, column = 1)

btn3 = Button(root, text = "BTN3", width = 12)
btn3.grid(row = 2, column = 0, sticky = "ew")
lbl3 = Label(root, width = 12)
lbl3.grid(row = 2, column = 1)

btn4 = Button(root, text = "BTN4", width = 12)
btn4.grid(row = 3, column = 0, sticky = "ew")
lbl4 = Label(root, width = 12)
lbl4.grid(row = 3, column = 1)

btn1.bind("<Button-1>", asc1)
btn2.bind("<Button-1>", asc2)
btn3.bind("<Button-1>", asc3)
btn4.bind("<Button-1>", asc4)




root.mainloop()