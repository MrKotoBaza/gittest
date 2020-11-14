from tkinter import *


tk = Tk()
def show(event):
    print(event.keysym)
tk.bind_all("<KeyPress>", show)

tk.mainloop()