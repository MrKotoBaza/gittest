from userclass import User
from systemclass import System

system = System("Synthesa")

user = User("kotobaza", system=system)


while True:
    string = input().lower()
    if string == "stop":
        break
    eval(string)
    