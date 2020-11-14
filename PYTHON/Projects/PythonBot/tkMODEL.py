import tkinter as tk
from tkinter import filedialog as fg

def initializateRootWindow():
    """
    Initializates Main Window in start the bot
    """
    pass

def initializateLoginWidow():
    """
    Initializates Login Window with Registration Button
    Registration Button changed Login Window with changeLoginWindow()
    """
    pass

def changeLoginWindow():
    """
    Changes ObjectsPositions in LoginWindow. Useing in registration Button
    """
    pass

def changeRootWindow():
    """
    Changes ObjectPositions in ROOTWindow. Useing after full login in system
    """
    pass
def initializateCalkWindow():
    """
    Initializates Calkulators Window.
    Calk with sin, coss, tg, ctg and reverse them
    """
    pass
def initializateCanvasWindow():
    """
    Initialisates Canvas Window for drawing.
    """
    pass
def initializateCinverterWindow():
    """
    initializates Converter Window
    """
    pass

def getfile():
    fileDB = fg.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
    return fileDB

def destroyWindow(win):
    """
    win = tkinter window == str()
    Destroyes windows
    """
    if win in globals():
        win.destroy()


