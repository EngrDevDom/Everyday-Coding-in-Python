# File  :   quadratic_6.py
# Desc  :   A program that computes the real roots of a quadratic equation. Version 5.0
#           Note: This program catches the exception.

import math

def main():

    print("This program finds the real solutions to a quadratic\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        discRoot = math.sqrt(b ** 2 - 4 * a * c)

        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print("\nThe solutions are:", root1, root2)

    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots.")
        else:
            print("Invalid coefficient given.")
    except:
        print("\nSomething went wrong, sorry!")

main()
