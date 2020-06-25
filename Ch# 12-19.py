# Ch 12
num1 = int(input("Please enter your first number : "))
num2 = int(input("Please enter your second number: "))
if num1 > num2:
    print(num1, ",", num2)
else:
    print(num2, ",", num1)

# Ch 13
num= int(input("Enter a value less than 20: "))
if num < 20:
    print("Thank you!")
else:
    print("Too high!")

# Ch 14
num = int(input("Enter a value between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you!")
else:
    print("Incorrect answer!")

# Ch 15
colour = input("Please enter your favorite color: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too.")
else:
    print("I don't like", colour, ", I prefer red.")

# Ch 16
raining = input("Is it raining? ")
if raining == "yes" or raining == "YES" or raining == "Yes":
    windy = input("Is it windy? ")
    if windy == "yes" or windy == "YES" or windy == "Yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day!")

# Ch 17
age = int(input("Please enter your age: "))
if age >= 18:
    print("You can vote.")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go Trick-or-Treating.")

# Ch 18
num = int(input("Please enter a number: "))
if num < 10:
    print("Too low!")
elif num >= 10 and num <= 20:
    print("Correct!")
else:
    print("Too high!")

# Ch 19
num = int(input("Please enter a number between (1, 2 or 3): "))
if num == 1:
    print("Thank you.")
elif num == 2:
    print("Well done!")
elif num == 3:
    print("Correct!")
else:
    print("Error message.")
