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

toolBar = Frame(root, bg="#A1A1A1")
toolBar.pack(side = TOP, fill = X)
btn1 = Button(toolBar, text = "Cut")
btn1.grid(row = 0, column = 0, padx = 2, pady = 2)
btn2 = Button(toolBar, text = "Copy")
btn2.grid(row = 0, column = 1, padx = 2, pady = 2)
btn3 = Button(toolBar, text = "Paste")
btn3.grid(row = 0, column = 2, padx = 2, pady = 2)

statusBar = Label(root, relief = SUNKEN, anchor = W, text = "Mission complete")
statusBar.pack(side = BOTTOM, fill = X)

root.geometry("700x400")
root.mainloop() 

