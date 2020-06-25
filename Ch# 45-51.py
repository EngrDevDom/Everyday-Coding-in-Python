# While loop

# Ch 45
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total += num
    print("The current total is: ", total)
print("The total is over 50.")

# Ch 46
value = 0
while value < 5:
    value += 1
    num = input("Enter a number: ")
print("The last number you've entered was a", num)

# Ch 47
num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number: "))
answer = num1 + num2
choice = "y"
while choice != "n":
    choice = input("Do you want to enter another number? (y/n): ")
    if choice == "y":
        newNum = int(input("Enter another number: "))
        answer += newNum
    else:
        input("Press <Enter> to see total.")
print("The total is", answer)

# Ch 48
count = 0
again = "y"
while again == "y":
    name = input("Enter the name you want to invite: ")
    print(name, "has now been invited.")
    count += 1
    again = input(print("Do you want to invite someboody else? (y/n): "))
print("Total of", count, "has been invited.")

# Ch 49
compNum = 50
num = 0
count = 0
while compNum != num:
    num = int(input("Enter a number: "))
    count += 1
    if compNum > num:
        print("Number is too low!")
    elif compNum < num:
        print("Number is too high!")
print("\nWell done, you took", count, "attempts.")

# Ch 50
num = int(input("Enter a number: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too low!")
    elif num > 20:
        print("Too high!")
    num = int(input("Try again!: "))
print("Thank you!")

# Ch 51
num = 10
while num > 0:
    print("There are", num, "green bottles hanging on the wall.")
    print(num, "green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall,")
    num -= 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print("There will be", num, "green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again!"))
print("There are no more green bottles hanging on the wall.")


