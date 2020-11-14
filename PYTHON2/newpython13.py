import tkinter as tk
root = tk.Tk()
root.title("Calk")
GlobalString = ""
frame = tk.Frame(root, bg = "lightgray")
frame.pack()
entry = tk.Entry(frame, bg = "white", width = 40, show = "0")
def addChar(event):
    global GlobalString
    global entry
    char = event.keysym
    if char == "equal":
        entry.configure(show=exec(GlobalString))
    elif char == "plus":
        GlobalString+="+"
        entry.configure(show=GlobalString)
    elif char == "minus":
        GlobalString+="-"
        entry.configure(show = GlobalString)
    elif char == "slash":
        GlobalString+="/"
        entry.configure(show = GlobalString)
    elif char in "1234567890":
        GlobalString+=char
        char = ""
        entry.configure(show = GlobalString)
    else:
        print("Wrong char")
entry.bind_all("<KeyPress>", addChar)
entry.pack()
root.mainloop()


