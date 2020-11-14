import tkinter as tk
root = tk.Tk()
pw = tk.PanedWindow(root, orient = 'vertical')
m = tk.Label(root, text="Heellloooo")
l = tk.Label(root, text="Woorld")
pw.add(m)
pw.add(l)
pw.pack()
root.mainloop()