# File  :   average2.py
# Desc  :   A program that gets the average the series of integers

def main():

    total = 0.0
    count = 0
    moredata = "yes"

    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        total += x
        count += 1
        moredata = input("Do you have more numbers (yes or no)? >> ")

    average = total / count

    print("\nThe average of the numbers is", average)

main()
