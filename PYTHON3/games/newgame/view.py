import tkinter as tk
import tkinter.ttk as ttk
import grid_model
import canvas_grid

def setup():
    global root, grid_view, start_button, clear_button, choice, option, grid

    grid = grid_model.GridModel(100, 100, r"C:\Users\Александра\Desktop\Основная папка\XXXXXXXXXXXXXXX\games\patterns")

    root = tk.Tk()

    root.title("The Game of Life")

    grid_view = canvas_grid.CanvasGrid(root, grid.width, grid.height, 5)
    grid_view.bind("<Button-1>", grid_handler)

    start_button = tk.Button(root, text = "Start", width = 12)
    start_button.bind("<Button-1>", start_handler)

    clear_button = tk.Button(root, text = "Clear", width = 12)
    clear_button.bind("<Button-1>", clear_handler)

    choice = tk.StringVar(root)
    choice.set("Choice a Pattern")

    option = ttk.OptionMenu(root,  choice, *grid.patterns, "random", command = option_handler)

    save_button = tk.Button(root, text="Save", width = 12)
    save_button.bind("<Button-1>", save_pattern)

    grid_view.grid(row = 0, columnspan = 3, padx = 20, pady = 20)
    start_button.grid(row = 1, column = 0, sticky = "W", padx = 20, pady = 20)
    option.grid(row = 2, column = 1, padx = 20, pady = 20)
    clear_button.grid(row = 1, column = 2, sticky = "E", padx = 20, pady = 20)
    save_button.grid(row = 1, column = 1, padx = 20, pady = 20)

def save_pattern(event):
    global start_button, grid, option
    grid.is_running = False
    start_button.configure(text = "Pause")

    grid.save_new_pattern()

    option.set_menu(*grid.patterns)

def option_handler(option):
    global start_button, grid, choice, grid_view
    grid.is_running = False
    start_button.configure(text="Start")

    selection = choice.get()
    
    if selection == "random":
        grid.randomize()

    if selection[-4:] == ".txt":
        grid.load_pattern_to_grid_model(selection)
        grid_view.reload_canvas(w = grid.width, h = grid.height, cellsize = 5)
        choice.set(selection)


    update()

def grid_handler(event):
    global grid_view, grid

    grid.is_running = False
    start_button.configure(text = "Start")
    

    x = int(event.x / grid_view.cell_size)
    y = int(event.y / grid_view.cell_size)

    if grid.grid_model[x][y] == 1:
        grid.grid_model[x][y] == 0
        grid_view.draw_cell(x, y, "white")
    else:
        grid.grid_model[x][y] = 1
        grid_view.draw_cell(x, y, "black")

def clear_handler(event):
    global grid, start_button
    grid.is_running = False
    for i in range(0, grid.height):
        for j in range(0, grid.width):
            grid.grid_model[i][j] = 0

    start_button.configure(text="Start")
    update()

def update():
    global grid_view, root, grid

    grid_view.delete("all")
    grid.update_grid()
    for i in range(0, grid.height):
        for j in range(0, grid.width):
            if grid.grid_model[i][j] == 1:
                grid_view.draw_cell(i, j, "black")

    if grid.is_running:
        root.after(grid.width, update)

def start_handler(event):
    global start_button, grid

    if grid.is_running:
        grid.is_running = False
        start_button.configure(text = "Start")
    else:
        grid.is_running = True
        start_button.configure(text = "Pause")
        update()

setup()
update()
root.mainloop()


#переделать систему сохранения паттернов