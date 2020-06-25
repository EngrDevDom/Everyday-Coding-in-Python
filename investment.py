# File  :   investment.py
# Desc  :   A program that uses a while loop to determince how long it takes
#           for an investment to double at a given interest rate.

def main():

    # annual interest rate
    rate = float(input("Enter the interest rate: >> "))

    # initial investment
    inival = float(input("Enter the initial investment: >> "))

    n = 0
    while futval != inival*2:
        n = n + 1
        futval = inival + (inival*rate)

    print("It takes", n, "years to double the initial investment.")

main()
