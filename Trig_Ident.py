"""
    File	      : Trig_Ident.py
    Description	  : This program aims to solve basic
                    trigonometric identities.
    Last Modified : 03/04/2020
    Author	      : Engr. Dom
"""
import math

print("Welcome to a program that solves basic Trigonometric Identities.")
print("1) Degree Mode 2) Radian Mode")
mode = input("Enter your preferred mode: ")     # Mode

# Degree Mode
if mode == '1':
    degrees = float(input("Enter a value of angle in degrees: "))
    radians = math.radians(degrees)     # Convert degrees to radians
    print("\n*** Trigonometric Identities ***")
    print("a)Sine\nb)Cosine\nc)Tangent\nd)Cosecant\ne)Secant\nf)Cotangent\n")
    choice = input("Enter your choice: ")
    if choice == 'a':       # Sine
        print("Sine of", degrees, " = ", math.sin(radians))
    elif choice == 'b':     # Cosine
        print("Cosine of", degrees, " = ", math.cos(radians))
    elif choice == 'c':     # Tangent
        print("Tangent of", degrees, " = ", math.tan(radians))
    elif choice == 'd':     # Cosecant
        print("Cosecant of", degrees, " = ", 1/math.sin(radians))
    elif choice == 'e':     # Secant
        print("Secant of", degrees, " = ", 1/math.cos(radians))
    elif choice == 'f':     # Cotangent
        print("Cotangent of", degrees, " = ", 1/math.tan(radians))
    else:
        print("Not a valid choice! Try again!")
        print(input("Press enter to quit."))

# Radian Mode
elif mode == '2':
    degrees = float(input("Enter a value of angle in degrees: "))
    print("\n*** Trigonometric Identities ***")
    print("a)Sine\nb)Cosine\nc)Tangent\nd)Cosecant\ne)Secant\nf)Cotangent\n")
    choice = input("Enter your choice: ")
    if choice == 'a':  # Sine
        print("Sine of", degrees, " = ", math.sin(degrees))
    elif choice == 'b':  # Cosine
        print("Cosine of", degrees, " = ", math.cos(degrees))
    elif choice == 'c':  # Tangent
        print("Tangent of", degrees, " = ", math.tan(degrees))
    elif choice == 'd':  # Cosecant
        print("Cosecant of", degrees, " = ", 1 / math.sin(degrees))
    elif choice == 'e':  # Secant
        print("Secant of", degrees, " = ", 1 / math.cos(degrees))
    elif choice == 'f':  # Cotangent
        print("Cotangent of", degrees, " = ", 1 / math.tan(degrees))
    else:
        print("Not a valid choice! Try again!")
        print(input("Press enter to quit."))

else:
    print("Not a valid input!")
    print(input("Press enter to quit."))