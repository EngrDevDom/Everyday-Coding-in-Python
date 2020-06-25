# File  :   Future_val.py
# Desc  :   A program to compute the value of an investment
#           carried 10 years into the future.

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the annual investment:- "))
    apr = eval(input("Enter the annual interest rate:- "))
    n = eval(input("Enter number of years:- "))

    for i in range(n):
        principal = principal * (1 + apr)

    print("The value of principal in 10 years is: ", principal)

main()
