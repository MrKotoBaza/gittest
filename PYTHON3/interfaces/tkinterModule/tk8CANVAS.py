from tkinter import *

root = Tk()

c1 = Canvas(root, width = 500, height = 500, cursor = "pencil", bg = "white")
c1.pack()

c1.create_line(250, 0, 250, 500, width = 3, fill = "red", arrow = LAST )
c1.create_line(0, 250, 500, 250, width = 3, fill = "blue", arrow = BOTH )
c1.create_rectangle(10, 10, 240, 240, fill = "green", outline = "red")
c1.create_polygon(260, 10, 490, 10, 400, 125, 490, 240, 260, 240, 350, 125, fill = "orange", smooth = 1)
c1.create_oval(10, 260, 240, 340, fill = "yellow",outline = "red", width = 3 )
c1.create_arc(10, 350, 90, 430, start = 0, extent = 270, fill = '#0000cc')
c1.create_arc(160, 350, 240, 430, start = 0, extent = 270, fill = '#000099', style = "chord")
c1.create_arc(80, 410, 160, 490, start = 0, extent = 270, style = "arc", outline = "#ff6600", width = 3)
c1.create_text(275, 330, text = "Tkinter \nit's a program \nwith window interface", font = ("Verdana", 12), anchor = "w", justify = "center", fill = "orange")





root.mainloop()