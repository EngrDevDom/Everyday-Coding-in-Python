# File  :   average4.py
# Desc  :   A program that gets the average the series of integers

def main():

    total = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >> ")

    while xStr != "":
        x = float(xStr)
        total += x
        count += 1
        xStr = input("Enter a number (<Enter> to quit) >> ")

    average = total / count

    print("\nThe average of the numbers is", average)

main()
