import tkinter as tk 
root = tk.Tk()
canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()

root.update()

def on_wasd(event):
    print("key pressed:", event.keysym, event.keycode)

canvas.bind_all("<Key>", on_wasd)

root.mainloop()
