# File  :   average6.py
# Desc  :   A program that gets the average the series of integers

def main():

    fileName = input("What file are the numbers in? >> ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0

    line = infile.readline()
    while line != "":
        total = total + float(line)
        count += 1
        line = infile.readline()

    average = total / count

    print("\nThe average of the numbers is", average)

main()