# File  :   wages.py
# Desc  :   A program to input the number of hours worked and the
#           hourly rate and calculate the total wages for the week.

def main():

    HOURS = float(input("Enter your number of hours: >> "))
    HOUR_RATE = float(input("Enter your hourly rate: >> "))

    if HOURS <= 40:
        # multiplier
        k = 1
    elif HOURS >= 40:
        # multiplier
        k = 1.3

    WAGE = HOURS * HOUR_RATE * k

    print("Your wage is", WAGE, "\nDone!")

main()
