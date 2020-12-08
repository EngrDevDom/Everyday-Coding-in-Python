""" Decision Tree Algorithm """

print("\n\t\t\t\tDecision Tree Algorithm")
print()
print("X ----------------------------------------------")
print("|\t\t\t\t\t\t\t\t\t\t\t\t|")
print("|\t\t\t\t\t\t\t\t\t\t\t\t|")
print("X --------------\t\t\t\t\t\t\t\tX ------")
print("|\t\t\t\t|\t\t\t\t\t\t\t\t|\t\t|")
print("|\t\t\t\t|\t\t\t\t\t\t\t\t|\t\t|")
print("|\t\t\t\tX ------\t\t\t\t\t\tG\t\tH")
print("|\t\t\t\t|\t\t|")
print("|\t\t\t\t|\t\t|")
print("X ------\t\tC\t\tX ------")
print("|\t\t|\t\t\t\t|\t\t|")
print("|\t\t|\t\t\t\t|\t\t|")
print("A\t\tB\t\t\t\tD\t\tX ------")
print("\t\t\t\t\t\t\t\t|\t\t|")
print("\t\t\t\t\t\t\t\t|\t\t|")
print("\t\t\t\t\t\t\t\tE\t\tF")
print()

count = 0

while (count < 9):
    # START
    print()
    print("************************* START *************************")
    print("\nAnswer the questions with Y or N.\n")

    # 1st Node
    x1 = input("Smaller than a Bicycle? ")
    if x1 == "Y" or x1 == "y":
        # 2nd Node
        x2 = input("Carnivore? ")
        if x2 == "Y" or x2 == "y":
            # 3rd Node
            x3 = input("Does it swim? ")
            if x3 == "Y" or x3 == "y":
                print("Piranha!\n")
                print("X")
                print("|")
                print("|")
                print("X")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("X")
                print("|")
                print("|")
                print("A")

            else:
                print("House Cat!\n")
                print("X")
                print("|")
                print("|")
                print("X")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("X ------")
                print("\t\t|")
                print("\t\t|")
                print("\t\tB")
        else:
            # 4th Node
            x4 = input("Does it fly? ")
            if x4 == "Y" or x4 == "y":
                print("Robin!")
            else:
                # 5th Node
                x5 = input("Does it swim? ")
                if x5 == "Y" or x5 == "y":
                    print("Salmon!")
                else:
                    # 6th Node
                    x6 = input("Mammal? ")
                    if x6 == "Y" or x6 == "y":
                        print("Mouse!")
                    else:
                        print("Virus")
    else:
        # 7th Node
        x7 = input("Does it swim? ")
        if x7 == "Y" or x7 == "y":
            print("Blue Whale!")
        else:
            # 8th Node
            print("Cow!")

    count += 1

    print("Count: ", count)
    print("*************************  END  *************************")

