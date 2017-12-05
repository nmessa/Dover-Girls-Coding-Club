##Hello world with functions
from turtle import *

def drawAnH():
    left(90)
    forward(100)
    back(50)
    right(90)
    forward(40)
    left(90)
    forward(50)
    back(100)

def drawAnI():
    forward(50)
    penup()
    forward(25)
    stamp()

def moveToNextLetter():
    penup()
    right(90)
    forward(40)
    left(90)
    pendown()
    
pensize(5)
shape("turtle")
color('red')
drawAnH()
moveToNextLetter()
drawAnI()

hideturtle()
done()
