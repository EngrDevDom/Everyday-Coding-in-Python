# File  :   maxn_best.py
# Desc  :   This program finds the maximum of a series of numbers.
#           This is the best way to do it.

def main():
    try:
        x1, x2, x3 = eval(input("Please enter three values: "))
        print("The largest value is", max(x1,x2,x3))
    except ValueError:
        print("Enter three values only idiot!")

main()
