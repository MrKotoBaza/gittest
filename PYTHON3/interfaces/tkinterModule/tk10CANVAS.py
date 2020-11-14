from tkinter import *
from math import sin, cos
root = Tk()
x = 0
def print_dot():
    global x
    y1 = sin(x)
    y2 = cos(x)

    root.after(5, print_dot)
    x+=0.03

    cvs.create_oval(25*x+10, 25*y1+100, 25*x+10, 25*y1+100, width = 1, outline = "red")
    cvs.create_oval(25*x+10, 25*y2+100, 25*x+10, 25*y2+100, width = 1, outline = "blue")
cvs= Canvas(root, width = 600, height = 200, bg="#fff")
cvs.pack()

cvs.create_line(10, 0, 10, 200, width = 2, arrow=BOTH, fill = "gray")
cvs.create_line(10, 100, 600, 100, width = 2, arrow=LAST, fill = "gray")

print_dot()

root.mainloop()