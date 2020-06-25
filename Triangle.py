# File  :   Triangle.py
# Desc  :   This program calculates the area of a triangle given the length of its
#           three sides a, b, and c.

import math

def main():
    a = float(input("Enter the value of the first side(a): "))
    b = float(input("Enter the value of the second side(b): "))
    c = float(input("Enter the value of the third side(c): "))

    S = (a+b+c)/2
    Area = math.sqrt(S*(S-a)*(S-b)*(S-c))

    print("The Area of the triangle is", Area)

main()