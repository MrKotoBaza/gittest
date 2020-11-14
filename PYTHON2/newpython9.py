import tkinter as tk 
import time
import random 

rootWidth = 500
rootHeight= 500

snakeItemWidth = 10
snakeColor1 = "red"
snakeColor2 = "yellow"
presentColor = "blue"

virtualWidth = rootWidth/snakeItemWidth
virtualHeight = rootHeight/snakeItemWidth

snakeX = 24
snakeY = 24
snakeNavX = 0
snakeNavY = 0

snakeList = []
snakeSize = 3

presentsList = []
presentsSize = 5

GameBunnung = 1

def presentsGenerator():
    global presentsSize
    global presentsList
    global virtualHeight
    global virtualWidth
    global presentColor
    for i in range(presentsSize):
        x = random.randrange(virtualWidth)
        y = random.randrange(virtualHeight)

        id1 =canvas.create_oval(x*snakeItemWidth, y*snakeItemWidth, x*snakeItemWidth+snakeItemWidth, y*snakeItemWidth+snakeItemWidth, fill = presentColor)

        presentsList.append([x, y, id1])



root = tk.Tk()
root.title("Змейка")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = tk.Canvas(root, width = rootWidth, height = rootHeight, bd = 0)
canvas.pack()

def checkFoundPresent():
    global snakeSize
    global presentsList
    newList = list(presentsList)
    for i in range(len(presentsList)):
        if presentsList[i][0] == snakeX and presentsList[i][1] == snakeY:
            snakeSize+=1
            canvas.delete(presentsList[i][2])

            newList.pop(i)
    presentsList = newList

def snakePaintItem(canvas, x, y):
    global snakeList

    id1 =canvas.create_rectangle(x*snakeItemWidth, y*snakeItemWidth, x*snakeItemWidth+snakeItemWidth, y*snakeItemWidth+snakeItemWidth, fill = snakeColor2)
    id2 =canvas.create_rectangle(x*snakeItemWidth+3, y*snakeItemWidth+3, x*snakeItemWidth+snakeItemWidth-3, y*snakeItemWidth+snakeItemWidth-3, fill = snakeColor1)
    
    snakeList.append([x, y, id1, id2])

def check_snake():
    global snakeList
    global snakeSize
    if len(snakeList) >= snakeSize:
        tempItem = snakeList.pop(0)

        canvas.delete(tempItem[2])
        canvas.delete(tempItem[3])

presentsGenerator()
snakePaintItem(canvas, 24, 24)

def gameOver():
    global GameBunnung
    GameBunnung = 0


def checkBorders():
    if snakeX >=virtualWidth or snakeY >= virtualHeight or snakeX <0 or snakeY <0:
        gameOver()

def checkBody(x, y):
    global snakeNavX
    global snakeNavY
    if not(snakeNavX == 0 and snakeNavY == 0):
        for i in range(len(snakeList)):
            if snakeList[i][0] == x and snakeList[i][1] == y:
                gameOver()

def snakeMove(event):
    global snakeX
    global snakeY
    global snakeNavX
    global snakeNavY
    if event.keysym == "Up":
        snakeNavX = 0
        snakeNavY = -1
        check_snake()
    elif event.keysym == "Down":
        snakeNavX = 0
        snakeNavY = 1
        check_snake()
    elif event.keysym == "Left":
        snakeNavX = -1
        snakeNavY = 0
        check_snake()
    elif event.keysym == "Right":
        snakeNavX = 1
        snakeNavY = 0
        check_snake()

    snakeX = snakeX+snakeNavX
    snakeY = snakeY+snakeNavY
    snakePaintItem(canvas, snakeX, snakeY)
    checkFoundPresent()


canvas.bind_all("<KeyPress-Left>", snakeMove)
canvas.bind_all("<KeyPress-Right>", snakeMove)
canvas.bind_all("<KeyPress-Up>", snakeMove)
canvas.bind_all("<KeyPress-Down>", snakeMove)

while GameBunnung:
    check_snake()
    checkFoundPresent()
    checkBorders()
    checkBody(snakeX+snakeNavX, snakeY+snakeNavY)
    snakeX = snakeX+snakeNavX
    snakeY = snakeY+snakeNavY
    snakePaintItem(canvas, snakeX, snakeY)
    root.update_idletasks()
    root.update()
    time.sleep(0.3)

def nothing(event):
    pass

canvas.bind_all("<KeyPress-Left>", nothing)
canvas.bind_all("<KeyPress-Right>", nothing)
canvas.bind_all("<KeyPress-Up>", nothing)
canvas.bind_all("<KeyPress-Down>", nothing)