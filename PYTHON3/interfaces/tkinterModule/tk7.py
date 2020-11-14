from tkinter import *
from tkinter.filedialog import *
def open_file():
    path = askopenfilename()
    file = open(path, "r")
    txt.insert(END, file.read())
    file.close()
def save_file():
    sf = asksaveasfilename()
    finaltext = txt.get(1.0, END)
    file = open(sf, "w")
    file.write(finaltext)
    file.close()
def exit_app():
    root.quite()

root = Tk()

mainmenu = Menu(root)
root.configure(menu = mainmenu)

firstItem = Menu(mainmenu, tearoff = 0)
mainmenu.add_cascade(label = "FIle", menu = firstItem)

firstItem.add_command(label = "Open", command = open_file)
firstItem.add_command(label = "Save", command = save_file)
firstItem.add_command(label = "Exit", command = exit_app)

txt = Text(root, width = 40, height = 30, font = 12)
txt.pack(expand = YES, fill = BOTH)


root.mainloop()
