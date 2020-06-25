# File  :   average5.py
# Desc  :   A program that gets the average the series of integers

def main():

    fileName = input("What file are the numbers in? >> ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0

    for line in infile:
        total = total + float(line)
        count += 1

    average = total / count

    print("\nThe average of the number is", average)

main()
