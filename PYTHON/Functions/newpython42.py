import tkinter as tk
from random import randint

WIDTH = 900
HEIGHT = 700

class Ball():

    def __init__(self, dx, dy, color):
        self.R = randint(5, 20)
        self.x = randint(self.R, WIDTH-self.R)
        self.y = randint(self.R, HEIGHT-self.R)
        self.dx = dx
        self.dy = dy
        self.color = color
        self.ball_id = CANVAS.create_oval(self.x-self.R, self.y-self.R, self.x+self.R, self.y+self.R, fill=color)

    def move(self):
        self.x += self.dx
        self.y +=self.dy
        if self.x +self.R> WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx

        if self.y +self.R >HEIGHT or self.y - self.R <=0:
            self.dy = -self.dy

    def show(self):
        CANVAS.move(self.ball_id, self.dx, self.dy)
    
    def checkInside(self, x, y):
        pass
    def checkCollision(self, ):
        pass

def tick():
    for s in range(len(balls)-1):
        balls[s].move()
        balls[s].show()
    ROOT.after(10, tick)

balls = [0]*100
colors = ["red", 'lime', 'blue', "orange"]

def main():
    global ROOT, CANVAS
    ROOT = tk.Tk()
    CANVAS = tk.Canvas(ROOT, width = WIDTH, height = HEIGHT)
    for l in range(len(balls)-1):
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(0, len(colors)-1)
        balls[l] =Ball(a, b, colors[c])
    ROOT.geometry(str(WIDTH)+"x"+str(HEIGHT))
    CANVAS.pack(fill = "both")
    tick()
    ROOT.mainloop()


main()