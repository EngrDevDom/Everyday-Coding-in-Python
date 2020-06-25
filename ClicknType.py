# File  :   ClicknType.py
# Desc  :   This program allows the user to label positions in a window
#           by typing a single keypress after each mouse click.

from graphics import *

def main():
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()

        label = Text(pt, key)
        label.draw(win)

main()
