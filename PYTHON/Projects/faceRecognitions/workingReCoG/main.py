import tkinter as tk
from CVtest import facerecogvideotest as ft
from facerecog import facerecogrealtime as fr

def goout():
    exit()

root = tk.Tk()
lb1 = tk.Label(root, text="Программа распознавания лица", font=["Arial", 16])
button1 = tk.Button(root, text="EXIT", command = goout)
button2 = tk.Button(root, text="Test", command = ft)
button3 = tk.Button(root, text="Start", command = fr)

lb1.pack()
button1.pack()
button2.pack()
button3.pack()

root.geometry("300x100")
root.mainloop()