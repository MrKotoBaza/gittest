from tkinter import *
root = Tk()
class Question:
    def __init__(self, main):
        self.entry1 = Entry(main, width = 3, font = 15)
        self.button1 = Button(main, text="Asc")
        self.label1 = Label(main, width = 27, font = 15)
        
        self.entry1.grid(row = 0, column = 0)
        self.label1.grid(row = 0, column = 2)
        self.button1.grid(row = 0, column = 1)

        self.button1.bind("<Button-1>", self.answer)

    def answer(self, event):
        txt = self.entry1.get()
        try:
            if int(txt)>=18:
                self.label1.configure(text = "Ok")
            else:
                self.label1.configure(text = "No, no, no")
        except ValueError:
            self.label1.configure(text = "Unresolved value")

q = Question(root)
root.title("Your возраст")

root.mainloop()