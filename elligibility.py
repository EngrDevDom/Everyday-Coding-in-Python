# File  :   elligibility.py
# Desc  :   A program that accepts a person's age and years of citizenship as
#           input and outputs their eligibility for the Senate and House.

def main():

    age = float(input("Enter your age: >> "))
    citizenship = float(input("Enter the years of your citizenship: >> "))

    if age == 30 and citizenship == 9:
        if age == 25 and citizenship == 7:
            print("You are eligible for US Senator and Representative.")
    else:
        print("You are eligible for any position.")

main()
