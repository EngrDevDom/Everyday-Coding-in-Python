# File  :   happy.py
# Desc  :   A program that greets a happy birthday using functions

def happy():
    print("Happy Birthday to you!")

def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear", person + ".")
    happy()

def main():
    sing("Fred")
    print()
    sing("Lucy")
    print()
    sing("Elmer")

main()
