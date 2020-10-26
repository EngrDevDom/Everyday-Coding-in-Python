# This program simulates the different types of Logic Gates

# AND GATE
def AND(A, B):
    if A == 1 and B == 1:
        return True
    else:
        return False

# OR GATE
def OR(A, B):
    if A == 1 or B == 1:
        return True
    else:
        return False

# NOT GATE
def NOT(A):
    if (A == 0):
        return True
    elif (A == 1):
        return False

# NAND GATE
def NAND(A, B):
    if A == 0 or B == 0:
        return True
    else:
        return False

# NOR GATE
def NOR(A, B):
    if A == 1 and B == 1:
        return False
    else:
        return True

# XOR GATE
def XOR(A, B):
    if A == 1 and B == 1:
        return False
    elif A == 0 and B == 0:
        return False
    else:
        return True

# XNOR GATE
def XNOR(A, B):
    if A == 1 and B == 1:
        return True
    elif A == 0 and B == 0:
        return True
    else:
        return False


# This is the main function
if __name__ == '__main__':
    print()

    # Print NOT Result
    print("       NOT GATE       ")
    print("+--------------------+")
    print("|    A\t\tOUTPUT\t |")
    print("|    False\t", NOT(0), "\t |")
    print("|    True\t", NOT(1), "\t |")
    print("+--------------------+")
    print()

    # Print AND Result
    print("       AND GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", AND(0, 0), "\t |")
    print("|    0   1\t", AND(0, 1), "\t |")
    print("|    1   0\t", AND(1, 0), "\t |")
    print("|    1   1\t", AND(1, 1), "\t |")
    print("+--------------------+")
    print()

    # Print OR Result
    print("       OR GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", OR(0, 0), "\t |")
    print("|    0   1\t", OR(0, 1), "\t |")
    print("|    1   0\t", OR(1, 0), "\t |")
    print("|    1   1\t", OR(1, 1), "\t |")
    print("+--------------------+")
    print()

    # Print NAND Result
    print("      NAND GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", NAND(0, 0), "\t |")
    print("|    0   1\t", NAND(0, 1), "\t |")
    print("|    1   0\t", NAND(1, 0), "\t |")
    print("|    1   1\t", NAND(1, 1), "\t |")
    print("+--------------------+")
    print()

    # Print NOR Result
    print("       NOR GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", NOR(0, 0), "\t |")
    print("|    0   1\t", NOR(0, 1), "\t |")
    print("|    1   0\t", NOR(1, 0), "\t |")
    print("|    1   1\t", NOR(1, 1), "\t |")
    print("+--------------------+")
    print()

    # Print XOR Result
    print("       XOR GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", XOR(0, 0), "\t |")
    print("|    0   1\t", XOR(0, 1), "\t |")
    print("|    1   0\t", XOR(1, 0), "\t |")
    print("|    1   1\t", XOR(1, 1), "\t |")
    print("+--------------------+")
    print()

    # Print XNOR Result
    print("      XNOR GATE       ")
    print("+--------------------+")
    print("|    A   B   OUTPUT  |")
    print("|    0   0\t", XNOR(0, 0), "\t |")
    print("|    0   1\t", XNOR(0, 1), "\t |")
    print("|    1   0\t", XNOR(1, 0), "\t |")
    print("|    1   1\t", XNOR(1, 1), "\t |")
    print("+--------------------+")
    print()

