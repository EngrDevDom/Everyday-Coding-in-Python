# File  :   Gregorian_epact.py
# Desc  :   This programs prompts the user for a 4-digit year
#           and then outputs the value of the epact.
#           Gregorian epact - is the number of days between January 1st and the
#                               previous new moon.

def main():
    year = eval(input("Enter the value of year: "))

    C = year // 100
    epact = (8 + (C // 4) - C + ((8*C+13) // 25) + 11(year%19))%30

    print("The value of Gregorian epact is", epact)

main()

