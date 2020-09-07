# File  :   Ladder.py
# Desc  :   This program determine the length of the ladder required to
#           reach a given height leaned.

import math

def main():
    angle = float(input("Enter the value of angle in degrees: "))
    radians = math.radians(angle)     # Convert degrees to radians

    height = float(input("Enter the value of height: "))
    length = height/math.sin(angle)

    print("The length of the ladder is", length)

main()

