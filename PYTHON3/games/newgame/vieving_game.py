import tkinter as tk
import tkinter.ttk as ttk
import canvas_grid 
import grid_model

class AdditionalApp(tk.Toplevel):
    def __init__(self, master, title, cellsize, grid):
        super().__init__(master)
        self.master = master
        self.grid = grid
        self.canvas = canvas_grid.CanvasGrid(self.master, grid.width,grid.height, cellsize)
        self.start_button = tk.Button(self.master, text = "Start", width = 12)
        self.clear_button = tk.Button(self.master, text = "Clear", width = 12)
        self.save_button = tk.Button(self.master, text="Save", width = 12)

        self.choiceVar = tk.StringVar(self.master)
        self.choiceVar.set("Choice a Pattern")
        self.option = ttk.OptionMenu(self.master,  self.choiceVar, *grid.patterns, "random")

        self.title(title)

        self.game_update()

    def pack(self):
        self.canvas.bind("<Button-1>", self.grid_handler)
        self.start_button.bind("<Button-1>", self.start_handler)
        self.clear_button.bind("<Button-1>", self.clear_handler)
        self.save_button.bind("<Button-1>", self.save_pattern)


        self.canvas.grid(row = 0, columnspan = 3, padx = 20, pady = 20)
        self.start_button.grid(row = 1, column = 0, sticky = "W", padx = 20, pady = 20)
        self.option.grid(row = 2, column = 1, padx = 20, pady = 20)
        self.clear_button.grid(row = 1, column = 2, sticky = "E", padx = 20, pady = 20)
        self.save_button.grid(row = 1, column = 1, padx = 20, pady = 20)

    def game_update(self):
        self.canvas.delete("all")
        self.grid.update_grid()
        for i in range(0, self.grid.height):
            for j in range(0, self.grid.width):
                if self.grid.grid_model[i][j] == 1:
                    self.canvas.draw_cell(i, j, "black")

        if self.grid.is_running:
            self.master.after(self.grid.width, self.game_update)


    def grid_handler(self, event):

        self.grid.is_running = False
        self.start_button.configure(text = "Start")
        

        x = int(event.x / self.canvas.cell_size)
        y = int(event.y / self.canvas.cell_size)

        if self.grid.grid_model[x][y] == 1:
            self.grid.grid_model[x][y] == 0
            self.canvas.draw_cell(x, y, "white")
        else:
            self.grid.grid_model[x][y] = 1
            self.canvas.draw_cell(x, y, "black")

    def option_handler(self, option):
        self.grid.is_running = False
        self.start_button.configure(text="Start")

        selection = self.choiceVar.get()
        
        if selection == "random":
            self.grid.randomize()

        if selection[-4:] == ".txt":
            self.grid.load_pattern_to_grid_model(selection)
            self.canvas.reload_canvas(w = self.grid.width, h = self.grid.height, cellsize = 5)
            self.choiceVar.set(selection)


        self.game_update()
    
    def save_pattern(self, event):
        self.grid.is_running = False
        self.start_button.configure(text = "Pause")

        self.grid.save_new_pattern()

        self.option.set_menu(*self.grid.patterns)

    def start_handler(self, event):
    

        if self.grid.is_running:
            self.grid.is_running = False
            self.start_button.configure(text = "Start")
        else:
            self.grid.is_running = True
            self.start_button.configure(text = "Pause")
            self.game_update()

    def clear_handler(self, event):
            
        self.grid.is_running = False
        for i in range(0, self.grid.height):
            for j in range(0, self.grid.width):
                self.grid.grid_model[i][j] = 0

        self.start_button.configure(text="Start")
        self.game_update()

    