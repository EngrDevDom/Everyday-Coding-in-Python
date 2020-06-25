""" Subprograms """

# Ch 118
def ask_value():
    num = int(input("Enter a number: "))
    return num

def count(num):
    n = 1
    while n <= num:
        print(n)
        n += 1

def main():
    num = ask_value()
    count(num)

main()


# Ch 119
import random

def pick_num():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low,high)
    return comp_num

def first_guess():
    print("I am thinking of a number...")
    guess = int(input("What am I thinking of: "))
    return guess

def check_answer(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, You win!")
            try_again = False
        elif comp_num > guess:
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too high, try again: "))

def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num, guess)

main()


# Ch 120
import random

# Option 1 : Addition
def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+", num2, "=")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers

# Option 2 : Subtraction
def subtraction():
    num3 = random.randint(25,50)
    num4 = random.randint(25,50)
    print(num3, "-", num4, "=")
    user_answer = int(input("Your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers

# Check and show the answer
def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Correct!")
    else:
        print("Incorrect, the answer is", actual_answer)

# Main Program
def main():
    print("1) Addition")
    print("2) Subtraction")
    selection = int(input("Enter 1 or 2: "))
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
    elif selection == 2:
        user_answer, actual_answer = subtraction()
        check_answer(user_answer, actual_answer)
    else:
        print("Incorrect selection.")

# Run the program
main()


# Ch 121

# Option 1 : Add Name
def add_name():
    name = input("Enter a new name: ")
    names.append(name)
    return name

# Option 2 : Change Name
def change_name():
    num = 0
    for x in names:
        print(num,x)
        num += 1
    select_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter new name: ")
    names[select_num] = name
    return names

# Option 3 : Delete Name
def delete_name():
    num = 0
    for x in names:
        print(num,x)
        num += 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

# Option 4 : View Names
def view_names():
    for x in names:
        print(x)
    print()

# Main Program
def main():
    again = "y"
    while again == "y":
        print("1) Add a name")
        print("2) Change a name")
        print("3) Delete a name")
        print("4) View names")
        print("5) Quit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = change_name()
        elif selection == 3:
            names = delete_name()
        elif selection == 4:
            names = view_names()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect option!")
        data = (names,again)

# List of Names
names = []

# Run the program
main()


# Ch 122
import csv

# Option 1 : Add to File
def AddtoFile():
    file = open("Salaries.csv","a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    new_record = name + ", " + str(salary) + "\n"
    file.write(str(new_record))
    file.close()

# Option 2 : View Records
def ViewRecords():
    file = open("Salaries.csv","r")
    for row in file:
        print(row)
    file.close()

# Menu
try_again = True
while try_again == True:
    print("1) Add to File")
    print("2) View all records")
    print("3) Quit program")
    print()
    selection = input("Enter the number of your selection: ")
    if selection == "1":
        AddtoFile()
    elif selection == "2":
        ViewRecords()
    elif selection == "3":
        try_again = False
    else:
        print("Incorrect option!")


# Ch 123
# Added delete option from Ch# 122

import csv

# Option 1 : Add to File
def AddtoFile():
    file = open("Salaries.csv","a")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    new_record = name + ", " + str(salary) + "\n"
    file.write(str(new_record))
    file.close()

# Option 2 : View Records
def ViewRecords():
    file = open("Salaries.csv","r")
    for row in file:
        print(row)
    file.close()

# Option 3 : Delete Records
def DeleteRecord():
    file = open("Salaries.csv","r")
    x = 0
    # Store the data in a temporary list
    tmp_list = []
    for row in file:
        tmp_list.append(row)
    file.close()
    for row in tmp_list:
        print(x,row)
        x += 1
    # Enter the row number to delete
    RowtoDelete = int(input("Enter the row number to delete: "))
    del tmp_list[RowtoDelete]
    # Update the data
    file = open("Salaries.csv","w")
    for row in tmp_list:
        file.write(row)
    file.close()

# Menu
try_again = True
while try_again == True:
    print("1) Add to File")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")
    print()
    selection = input("Enter the number of your selection: ")
    if selection == "1":
        AddtoFile()
    elif selection == "2":
        ViewRecords()
    elif selection == "3":
        DeleteRecord()
    elif selection == "4":
        try_again = False
    else:
        print("Incorrect option!")

