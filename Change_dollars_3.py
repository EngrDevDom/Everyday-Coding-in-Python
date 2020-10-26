# File  :   Change_dollars_3.py
# Desc  :   A program to calculate the value of some change in dollars

def main():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters : "))
    dimes = int(input("Dimes    : "))
    nickels = int(input("Nickels  : "))
    pennies = int(input("Pennies  : "))

    total = quarters*25 + dimes*10 + nickels*5 + pennies

    print()
    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

main()
