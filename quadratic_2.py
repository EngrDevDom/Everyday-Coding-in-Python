# File  :   quadratic_2.py
# Desc  :   A program that computes the real roots of a quadratic equation. Version 2.0
#           Note: This program crashes if the equation has no real roots.

import math

def main():

    print("This program finds the real solutions to a quadratic\n")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = math.sqrt(b*b - 4*a*c)
    if discrim >= 0:
        root1 = (-b + discrim) / (2*a)
        root2 = (-b - discrim) / (2*a)

        print("\nThe solutions are:", root1, root2)

main()
