# File  :   Click.py
# Desc  :   Getting Mouse Clicks coordinates

from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())

main()
