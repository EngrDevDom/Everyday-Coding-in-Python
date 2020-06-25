# File  :   Sum_of_n.py
# Desc  :   This program calculates the sum of first n natural numbers
#           where the value of n is provided by the user.

def main():
    a = int(input("Enter the number of digits to be added: "))

    for i in range(a):
        a = a + i

    print("The Sum of digits is", a)

main()