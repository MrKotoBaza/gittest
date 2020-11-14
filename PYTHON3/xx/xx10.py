import requests
import json
import turtle
import time


def move_iss(lat, long):
    global iss
    iss.penup()
    iss.goto(lat, long)
    iss.pendown()

screen = turtle.Screen()
screen.setup(1200, 700)
screen.bgpic("images/earth3.gif")
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()

url = "http://api.open-notify.org/iss-now.json"

def running():
    global url
    response = requests.get(url)

    response_dict = json.loads(response.text)

    position = response_dict["iss_position"]

    move_iss(float(position["latitude"]), float(position["longitude"]))
        
    print(response)
    widget = turtle.getcanvas()
    widget.after(5000, running)

running()


turtle.mainloop()