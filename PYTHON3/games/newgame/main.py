import vieving_game as view
import tkinter as tk
import grid_model

def setup():
    grid = grid_model.GridModel(100, 100, r"C:\Users\Александра\Desktop\Основная папка\XXXXXXXXXXXXXXX\games\patterns")

    root = tk.Tk()

    app = view.AdditionalApp(root, "Game of Life", 5, grid)

    

    root.mainloop()






