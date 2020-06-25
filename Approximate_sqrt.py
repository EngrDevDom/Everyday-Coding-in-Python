# File  :   Approximate_sqrt.py
# Desc  :   This program approximates the value of the square root of a given number,
#           and then see how close your guess is.

import math

def main():
    x = int(input("Enter the value of x: "))

    guess = x/2
    y = (guess + (x/guess))/2

    print("The approximate value of square root is: ", y)

    error = math.sqrt(x) - y

    print("The exact value of", x, "is", math.sqrt(x))
    print("The error is: ", error)

main()