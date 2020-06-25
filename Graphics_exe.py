# File  :   Graphics_exe.py
# Desc  :   This is an exercise program to determine its output

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(1, 25), Point(26, 50))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()

main()
