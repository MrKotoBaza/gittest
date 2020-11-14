from tkinter import *
from tkinter.messagebox import *
root = Tk()

btn1 = Button(root, text="Click me", font =15, command = lambda: showinfo("showInfo", "Info"))
btn2 = Button(root, text="Warning", font = 15, command =lambda: showwarning("showWarning", "Warning"))
btn3 = Button(root, text="Error", font = 15, command =lambda: showerror("showError", "Error"))

btn1.grid(row = 0, column = 0, sticky = "ew")
btn2.grid(row = 1, column = 0, sticky = "ew")
btn3.grid(row = 2, column = 0, sticky = "ew")

root.mainloop()