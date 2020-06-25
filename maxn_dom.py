# File  :   maxn_dom.py
# Desc  :   This program finds the maximum of a series of numbers.
#           Note: This is my solution.

def main():

    n = int(input("How many numbers are there? >> "))
    x = input("Enter the numbers separated by ',' >> ")

    for i in range(n):
        y = x.split(',')
        y.sort()
        z = y[n-1]

    print("The largest value is", z)

main()
