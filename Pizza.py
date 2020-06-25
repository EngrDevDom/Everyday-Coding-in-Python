# File  :   Pizza.py
# Desc  :   This program calculates the cost per-square-inch of a pizza,
#           given it's diameter and price

import math

def main():
    diameter = eval(input("Enter the Diameter(inch): "))
    price = eval(input("Enter the Price($): "))

    area = (math.pi*diameter*diameter)/4
    cost = price/area

    print("The cost per-square-inch of the pizza is $", cost)

main()