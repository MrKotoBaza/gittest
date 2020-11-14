import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, width = 540, height = 340)

canvas.create_rectangle(50, 50, 400, 300, fill = "blue")

canvas.pack()

win.update()

canvas.postscript(file = "xxxxxx.ps", colormode = "color")

#работа с ImageMagic