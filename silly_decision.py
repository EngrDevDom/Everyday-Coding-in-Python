# File  :   silly_decision.py

def main():

    a, b, c = eval(input("Enter three numbers: "))

    if a > b:
        if b > c:
            print("Spam Please!")
        else:
            print("It's a late parrot!")
    elif b > c:
        print("Cheese Shoppe")
        if a >= c:
            print("Cheddar")
        elif a < b:
            print("Gouda")
        elif c == b:
            print("Swiss")
    else:
        print("Trees")
        if a == b:
            print("Chestnut")
        else:
            print("Larch")

    print("Done!")

main()
