# Fibonacci Sequence

nTerms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 1
if nTerms <= 0:
    print("Please enter a positive integer.")
elif nTerms == 1:
    print("Fibonacci sequence up to", nTerms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")

    while count < nTerms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
