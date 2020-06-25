# Ch 35
name = input("Enter your name: ")
for i in range(3):
    print(name)

# Ch 36
name = input("Enter your name: ")
num = int(input("Enter a number: "))
for i in range(num):
    print(name)

# Ch 37
name = input("Enter your name: ")
for i in range(len(name)):
    print(name[i])

# Ch 38
num = int(input("Enter a number: "))
name = input("Enter your name: ")
for x in range(0, num):
    for i in name:
        print(i)

# Ch 39
num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)

# Ch 40
num = int(input("Enter a number: "))
for i in range(50, num-1, -1):
    print(i)

# Ch 41
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0,num):
        print(name)
else:
    for i in range(0,3):
        print("Too high!")

# Ch 42
total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number included? (y/n): ")
    if ans == "y":
        total += num
print(total)

# Ch 43
direction = input("Enter a direction up or down? (u/d): ")
if direction == "u":
    topNum = int(input("Enter a top number: "))
    for i in range(1, topNum+1, 1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand!")

# Ch 44
people = int(input("Enter the number of people invited: "))
if people < 10:
    for i in range(people):
        name = input("Enter the name: ")
        print(name, "has been invited.")
elif people >= 10:
    print("Too many people!")

