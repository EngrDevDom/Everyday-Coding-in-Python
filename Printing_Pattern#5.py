# Printing_Pattern 5

def pattern(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end=" ")
        print("\r")

pattern(5)
