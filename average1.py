# File  :   average1.py
# Desc  :   A program that gets the average the series of integers

def main():

    n = int(input("How many numbers do you have? >> "))
    total = 0.0

    for i in range(n):
        x = float(input("Enter a number >> "))
        total += x

    average = total / n

    print("\nThe average of the numbers is", average)

main()
