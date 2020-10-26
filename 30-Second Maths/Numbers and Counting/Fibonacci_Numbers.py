# Enter the nth term
n = int(input("Enter the nth term of Fibonnaci: "))

def main():
    a, b = 1, 1
    while a < n:
        a, b = b, a+b
    print("The", n, "th term of the Fibonacci is", a)

# Write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

main()
fib(n)

