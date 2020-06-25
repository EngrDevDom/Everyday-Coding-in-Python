# File  :   Fibonacci.py
# Desc  :   This program computes the nth Fibonaaci number where n
#           is a value input by the user.

def main():
    n = int(input("Enter the nth term of Fibonnaci: "))

    a, b = 1, 1
    while a < n:
        a, b = b, a+b

    print("The", n, "th term of the Fibonacci is", a)

main()
