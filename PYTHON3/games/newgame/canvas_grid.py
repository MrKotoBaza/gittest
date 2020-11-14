import tkinter as tk

class CanvasGrid(tk.Canvas):
    def __init__(self, m, w, h, cellsize, background = "white", borderw = 0):
        super().__init__(m, width = w*cellsize, height = h*cellsize, bg = background, borderw = borderw)
        self.cell_size = cellsize
        self.master = m

    def draw_cell(self, x, y, color):
        if color == "black":
            outline = "gray"
        if color == "white":
            outline = "white"

        self.create_rectangle(x*self.cell_size, 
                            y*self.cell_size, 
                            x*self.cell_size+self.cell_size, 
                            y*self.cell_size+self.cell_size, 
                            fill = color, 
                            outline = outline)
    
    def reload_canvas(self, w = None, h = None, cellsize = None):
        if w and h and cellsize:
            self.configure(width = w*cellsize)
            self.configure(height = h*cellsize)
        else:
            print("Not normal value of width/height/cell size")

