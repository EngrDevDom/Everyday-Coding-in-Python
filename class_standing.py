# File  :   class_standing.py
# Desc  :   A program that calculates class standing from the
#           number of credits earned.

def main():

    credit = eval(input("Enter your number of credits: >> "))
    standing = ''

    if credit > 0  or credit <= 6:
        standing = 'Freshman'
    elif credit <= 7 or credit <= 15:
        standing = 'Sophomore'
    elif credit == 16 or credit <= 25:
        standing = 'Junior'
    elif credit >= 26:
        standing = 'Senior'

    print("Your standing is", standing)

main()
