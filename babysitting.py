# File  :   babysitting.py
# Desc  :   A program that calculates the total babysitting bill.

def main():

    starting_time = float(input("Enter the starting time: >> "))
    ending_time = float(input("Enter the ending time: >> "))

    # initial babysitting charge
    k = 0

    if starting_time > 0 and ending_time < 9:
        k = 2.50
    elif ending_time > 9:
        k = 1.50

    # No. of hours
    n = ending_time - starting_time

    # calculation
    total = n * k

    print("Total charge is $", total)

main()
