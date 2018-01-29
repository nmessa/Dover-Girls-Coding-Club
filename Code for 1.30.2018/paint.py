## Drawing Program
## Author: nmessa

##we need to modify this program so it closes the shape
##how can we do this?

from graphics import *

win = GraphWin("Drawing Program", 1024, 768)
win.setCoords(0.0, 0.0, 10.0, 10.0)

p1 = win.getMouse()
while True:
    p2 = win.getMouse()
    aLine = Line(p1, p2)
    aLine.setFill('red')
    aLine.draw(win)
    p1 = p2




