from tkinter import *
root = Tk()

def newWin():
    win = Toplevel(root)
    label1 = Label(win, text="Text in window toop level", font = 20)
    label1.pack()

def exitApp():
    root.destroy()
mainMenu = Menu(root)
root.configure(menu = mainMenu)

firstItem = Menu(mainMenu, tearoff =0)
mainMenu.add_cascade(label = "File", menu = firstItem)
firstItem.add_command(label = "New", command = newWin)
firstItem.add_command(label = "Exit", command = exitApp)

secondItem = Menu(mainMenu, tearoff =0)
mainMenu.add_cascade(label = "Edit", menu = secondItem)
secondItem.add_command(label = "File1")
secondItem.add_command(label = "File2")
secondItem.add_command(label = "File3")
secondItem.add_separator()
secondItem.add_command(label = "File4")





root.mainloop()
