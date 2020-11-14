import tkinter as tk 
import random
import time

class Object():
    def __init__(self, Coords):
        self.Coords = Coords
        
class polygonPoints(Object):
    def __init__(self, Coords):
        Object.__init__(self, Coords)
        self.obj = c.create_oval(*self.Coords, fill="red", outline = "red")

class startPoint(Object):
    def __init__(self, Coords):
        Object.__init__(self, Coords)
        self.obj = c.create_oval(*self.Coords, fill = "blue", outline = "blue")

class othersPoints(Object):
    def __init__(self, Coords):
        Object.__init__(self, Coords)
        self.obj = c.create_oval(*self.Coords, fill="green", outline = "green")

def generateStartPoint():
    x = random.randint(1, 679)
    y = random.randint(1, 589)
    coords = [x, y, x+5, y+5]
    Coordinates["p0"] = coords
    newStartPoint = startPoint(coords)

def generatePolygon(val):
    val +=1
    i = 1
    generateStartPoint()
    while i<val:
        x = random.randint(1, 679)
        y = random.randint(1, 589)
        coords = [x, y, x+7, y+7]
        Coordinates["p" + str(i)] = coords
        point = polygonPoints(coords)
        i+=1

def drawSerpynski():
    num = random.randint(1, mainNum)
    newX = (Coordinates["p0"][0] + Coordinates["p"+str(num)][0])/2
    newY = (Coordinates["p0"][1] + Coordinates["p"+str(num)][1])/2
    newPoint = othersPoints([newX, newY, newX+1, newY+1])
    Coordinates["p0"] = [newX, newY]
    #updateCanvas()

def updateCanvas():
    c.update()
    time.sleep(0.00000000001)


root = tk.Tk()
root.geometry("700x600")
root.title("SerpinskyAngle")
c = tk.Canvas(root, width=680, heigh = 590, bg = "white")
c.pack()
mainNum = 3
Coordinates = {}
generatePolygon(mainNum)
for s in range(20000):
    drawSerpynski()
root.mainloop()

