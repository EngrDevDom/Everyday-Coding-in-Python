# Random

# Ch 52
import random

num = random.randint(1, 100)
print(num)

# Ch 53
import random

fruit = random.choice(['apple', 'mango', 'water melon', 'orange', 'grapes'])
print(fruit)

# Ch 54
import random

coin = random.choice(['h', 't'])
guess = input("Enter (h)eads or (t)ails : ")
if guess == coin:
    print("You win!")
else:
    print("Bad luck.")
print("The coin is",coin)

# Ch 55
import random

num = random.randint(1,6)
guess = int(input("Enter a number between 1 and 5: "))
if guess == num:
    print("Well done!")
elif guess > num:
    print("Too high!")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct!")
    else:
        print("You lose.")
elif guess < num:
    print("Too low!")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct!")
    else:
        print("You lose.")

# Ch 56
import random

num = random.randint(1,10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
        print("Correct! The number is", num)

# Ch 57
import random

num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
        print("Correct! The number is", num)
    elif guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high!")

# Ch 58
import random

score = 0
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print(num1, "+", num2, "=")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score += 1
print("You scored", score, "out of 5.")

# Ch 59
import random

colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from (red, blue, green, white or pink): ")
tryAgain = True
while tryAgain == True:
    theirChoice = input("Enter a colour: ")
    theirChoice = theirChoice.lower()
    if colour == theirChoice:
        print("Well done!")
        tryAgain = False
    else:
        if colour == "red":
            print("I bet you are seeing RED right now!")
        elif colour == "blue":
            print("Don't feel BLUE.")
        elif colour == "green":
            print("I bet you are GREEN with envy right now.")
        elif colour == "white":
            print("Are you WHITE as a sheet, as you didn't guess correctly?")
        elif colour == "pink":
            print("Shame you are not feeling in the PINK, as you got it wrong!")

