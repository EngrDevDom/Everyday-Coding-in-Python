"""
    File	      : Calculus.py
    Description	  : This program aims to solve common
                    calculus derivatives and integrals.
    Last Modified : 03/08/2020
    Author	      : Engr. Dom
"""
import math

print("********* Calculus *********")
print("1) Differential\n2) Integral\n")
category = eval(input("Enter your choice: "))

# Differential
if category == 1:
    print("\nFunctions:")
    print("a)sin(x)  b)cos(x)  c)tan(x)\nd)sec(x)  e)csc(x)  f)cot(x)\ng)a^(x)   h)e^(x)   i)ln(x)")
    choice = input("\nChoose function above: ")
    print()
    if choice == 'a':
        print("The derivative of sin(x) is cos(x).")
    elif choice == 'b':
        print("The derivative of cos(x) is -sin(x).")
    elif choice == 'c':
        print("The derivative of tan(x) is sec^2(x).")
    elif choice == 'd':
        print("The derivative of sec(x) is sec(x)tan(x).")
    elif choice == 'e':
        print("The derivative of csc(x) is -csc(x)cot(x).")
    elif choice == 'f':
        print("The derivative of cot(x) is -cot^2(x).")
    elif choice == 'g':
        print("The derivative of a^(x) is a^(x)*ln(a)")
    elif choice == 'h':
        print("The derivative of a^(x) is e^(x).")
    elif choice == 'i':
        print("The derivative of ln(x) is 1/x.")

# Integral
elif category == 2:
    print("Choose function above: ")
    print("Integral of ")
# Invalid
else:
    print("Not a valid input!")
    print(input("Press enter to quit."))