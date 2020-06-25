# File  :   event_loop2.py
# Desc  :   A program that simply opens up a graphics window and allows the
#           use to change its color by typing different keys.

from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    pass

def main():
    win = GraphWin("Click and Type", 500, 500)

    # Event Loop : handle key presses and mouse clicks until the user
    #               presses the "q" key
    while True:
        key = win.checkKey()
        if key == "q":  # exit loop
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()

main()
