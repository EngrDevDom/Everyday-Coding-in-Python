# File  :   Molecular.py
# Desc  :   This program calculates the molecular weight in (grams-per-mole).
#           Prompts the user to enter number of hydrogen, carbon and oxygen atoms.

H = 1.00794
C = 12.0107
O = 15.9994

def main():
    hydrogen = eval(input("Enter the number of hydrogen: "))
    carbon = eval(input("Enter the number of carbon: "))
    oxygen = eval(input("Enter the number of oxygen: "))

    molecular = H*hydrogen + C*carbon + O*oxygen
    print("The molecular weight is", molecular)

main()