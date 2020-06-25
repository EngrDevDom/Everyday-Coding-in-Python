# File  :   Distance.py
# Desc  :   This program accepts two points and determines the distance between them.

import math

def main():
    x1, y1 = eval(input("Enter first coordinate.(x1, y1): "))
    x2, y2 = eval(input("Enter second coordinate.(x2, y2): "))

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print("The distance between two points is:", distance)

main()