import tkinter as tk
import time
import random

root = tk.Tk()
root.title("Snake")
root.resizable(0, 0)

#основные размеры
rootW = 500
rootH = 500
rootSize = 10

#значения виртуальной сетки
virtualW = rootW/rootSize
virtualH = rootH/rootSize

#переменные для самой змейка
colors = ["red", "yellow", "blue"]
snakeList = []
presentsList = []
presentsSize = 10
snakeX = virtualW//2
snakeY = virtualH//2
navSnakeX = 0
navSnakeY = 0

counter = 0
snakeSize = 3

GameRunning = True
canvas = 0
def canvasGeneration():
    global canvas
    canvas = tk.Canvas(root, width = rootW, height = rootH, bg = "white")
    canvas.pack()

    canvas.bind_all("<KeyPress-Left>", snakeMove)
    canvas.bind_all("<KeyPress-Right>", snakeMove)
    canvas.bind_all("<KeyPress-Up>", snakeMove)
    canvas.bind_all("<KeyPress-Down>", snakeMove)

def canvasRegeneration():
    canvas.pack()
    canvas.delete("all")

def paintSnakeItem(canvas, x, y):
    """
    Рисует элемент змейки (квадрат) в холсте на указанных координатах
    
    canvas - объект холста
    x, y - координаты в rootSize, на которых будет верхний левый угол элемента
    """
    global snakeList

    id1 =canvas.create_rectangle(x*rootSize, y*rootSize, x*rootSize+rootSize, y*rootSize+rootSize, fill = colors[0])
    id2 =canvas.create_rectangle(x*rootSize+3, y*rootSize+3, x*rootSize+rootSize-3, y*rootSize+rootSize-3, fill = colors[1])
    
    snakeList.append([x, y, id1, id2])

def snakeMove(event):
    """
    Осуществляет изменение направления движения
    """
    global snakeX
    global snakeY
    global navSnakeY
    global navSnakeX
    if event.keysym == "Up":
        navSnakeX = 0
        navSnakeY = -1
        checkSnakeLen()
    elif event.keysym == "Down":
        navSnakeX = 0
        navSnakeY = 1
        checkSnakeLen()
    elif event.keysym == "Left":
        navSnakeX = -1
        navSnakeY = 0
        checkSnakeLen()
    elif event.keysym == "Right":
        navSnakeX = 1
        navSnakeY = 0
        checkSnakeLen()

    #snakeX = snakeX+navSnakeX
    #snakeY = snakeY+navSnakeY

def checkSnakeLen():
    """
    Проверяет длинну змейки, и удаляет ее самый старый элемент, создавая эффект движения
    """
    global snakeList
    global snakeSize

    if len(snakeList) >= snakeSize:
        tempItem = snakeList.pop(0)
        
        canvas.delete(tempItem[2])
        canvas.delete(tempItem[3])

def checkBorders():
    if snakeX >= virtualW-1 or snakeX <0 or snakeY >= virtualH-1 or snakeY <0:
        gameOver()

def gameOver():
    global GameRunning 
    global navSnakeX
    global navSnakeY
    GameRunning = 0
    navSnakeX = 0
    navSnakeY = 0
    print("You're dead. Game over")

    canvas.pack_forget()
    reloadGame()

def checkSnakeBody(x, y):
    global navSnakeX
    global navSnakeY
    global snakeList
    if not(navSnakeX == 0 and navSnakeY == 0):
        for i in range(len(snakeList)):
            if snakeList[i][0] == x and snakeList[i][1] == y:
                gameOver()

def presentsGeneration():
    global presentsSize
    global presentsList
    global virtualH
    global virtualW
    for i in range(presentsSize):
        x = random.randrange(1, virtualW-1)
        y = random.randrange(1, virtualH-1)

        id1 =canvas.create_oval(x*rootSize, y*rootSize, x*rootSize+rootSize, y*rootSize+rootSize, fill = colors[2])

        presentsList.append([x, y, id1])

def checkFindingPresent():
    global snakeSize
    global presentsList
    global counter
    newList = list(presentsList)
    for i in range(len(presentsList)):
        if presentsList[i][0] == snakeX and presentsList[i][1] == snakeY:
            snakeSize+=1
            canvas.delete(presentsList[i][2])
            newList.pop(i)
            counter += 1

    presentsList = newList

def globalGameCycle():
    global snakeX
    global snakeY
    global navSnakeX
    global navSnakeY
    global canvas
    presentsGeneration()
    #оснвной цикл
    while GameRunning:
        if len(presentsList) == 0:
            presentsGeneration()
        checkSnakeLen()
        checkFindingPresent()
        checkBorders()
        #checkPresents()
        checkSnakeBody(snakeX+navSnakeX, snakeY+navSnakeY)
        snakeX = snakeX+navSnakeX
        snakeY = snakeY+navSnakeY
        paintSnakeItem(canvas, snakeX, snakeY)
        root.update_idletasks()
        root.update()
        time.sleep(0.15)

def gameCycle():
    global frame
    frame.destroy()
    canvasGeneration()
    globalGameCycle()

def gameCycle2():
    global frame
    frame.destroy()
    canvasRegeneration()
    globalGameCycle()

def reloadGame():
    global frame
    global GameRunning
    global counter
    GameRunning = 1
    print(counter)
    frame = tk.Frame(root, width = rootW, height = rootH)
    frame.pack()
    gameName1 = tk.Label(frame, text = "Snake", fg = "lime", font = "Arial 24", justify = "center")
    gameName2 = tk.Label(frame, text = "Game", fg = "red", font = "Arial 20", justify = "center")

    counterLabel = tk.Label(frame, text="Your presents: {}".format(counter), font = "Arial 12", justify = "center")
    startButton = tk.Button(frame, text="Restart", justify = "center", font = "Arial 30", padx = 20, pady = 8, command = gameCycle2)

    gameName1.pack()
    gameName2.pack()
    counterLabel.pack()
    startButton.pack()
    counter = 0

def loadGame():
    global frame
    frame = tk.Frame(root, width = rootW, height = rootH)
    frame.pack()
    gameName1 = tk.Label(frame, text = "Snake", fg = "lime", font = "Arial 24")
    gameName2 = tk.Label(frame, text = "Game", fg = "red", font = "Arial 16")

    startButton = tk.Button(frame, text="Start", justify = "center", font = "Arial 30", padx = 20, pady = 8, command = gameCycle)

    gameName1.pack()
    gameName2.pack()
    startButton.pack()

loadGame()


root.mainloop()


