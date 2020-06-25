# File  :   Approximate_pi.py
# Desc  :   This program approximates the value of pi by summing terms,
#           prompts the user for n, the number of terms to sum and then
#           output the sum of the first n terms of this series.

import math

def main():
    n = eval(input("Enter the number of terms: "))

    for i in range(n):

        n = 4*(1 + (-1)**n/(2*i+1))

    print("The approximate value of pi is", n)

    error = math.pi - n
    print("The error is ", error)

main()
