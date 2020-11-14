import tkinter as tk
from random import randint

def canvasClicker(event):
    global ball1
    print("Hello World! x=", event.x, "y=", event.y)
    R = randint(20, 50)
    ball1 = canvas.create_oval(event.x-R, event.y-R, event.x+R, event.y+R, fill="green")
    tick()

def tick():
    canvas.move(ball1, +1, +1)
    root.after(150, tick)

def main():
    global root, canvas
    root = tk.Tk()
    root.geometry("800x600")
    canvas = tk.Canvas(root, )
    canvas.bind("<Button-1>", canvasClicker)
    canvas.pack(fill = "both")
    root.mainloop()

main()