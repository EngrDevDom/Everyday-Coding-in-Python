# File  :   Sphere.py
# Desc  :   This program calculates the Volume and Surface Area of a sphere,
#           given it's radius.

import math

def main():
    radius = eval(input("Enter the radius of the circle: "))

    Volume = (4/3)*math.pi*radius*radius*radius
    Area = 4*math.pi*radius*radius

    print("The Volume of the sphere is", Volume)
    print("The Area of the sphere is", Area)

main()

