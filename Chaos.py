# File  :   Chaos.py
# Desc  :   A simple program illustrating chaotic behavior
# General Form: k(x)(1-x)

def main():
    print("This program illustrates a chaotic function.")
    x, y = eval(input("Enter two numbers between 0 and 1 :- "))
    n = eval(input("How many numbers should I print? :- "))

    for i in range(n):
        x = 3.9 * x * (1-x)     # k = 3.9 in this case
        y = 3.9 * y * (1 - y)   # k = 2.0
        print(x, "---", y)

main()
