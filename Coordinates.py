# File  :   Coordinates.py
# Desc  :   This program calculates the slope of a line through two points.

def main():
    x1, y1 = eval(input("Enter first coordinate.(x1, y1): "))
    x2, y2 = eval(input("Enter second coordinate.(x2, y2): "))

    slope = (y2-y1)/(x2-x1)

    print("The slope of the line is :", slope)

main()