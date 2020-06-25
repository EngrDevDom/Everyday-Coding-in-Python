# File  :   average3.py
# Desc  :   A program that gets the average the series of integers

def main():

    total = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit) >> "))

    while x >= 0:
        total += x
        count += 1
        x = float(input("Enter a number (negative to quit) >> "))

    average = total / count

    print("\nThe average of the numbers is", average)

main()
