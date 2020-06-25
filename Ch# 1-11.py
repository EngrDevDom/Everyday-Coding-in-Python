# Ch 1
firstname = input("Please enter your first name: ")
print("Hello", firstname)

# Ch 2
firstname = input("Please enter you first name: ")
surname = input("Please enter your surname: ")
print("Hello", firstname, surname)

# Ch 3
num1 = int(input("Please enter your first number : "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number : "))

answer = num1+num2
print("The answer is", answer)

# Ch 4
num1 = int(input("Please enter your first number : "))
num2 = int(input("Please enter your second number: "))
answer = num1+num2

# Ch 5
num1 = int(input("Please enter your first number : "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third numer  :"))
answer = (num1+num2)*num3
print("The answer is", answer)

# Ch 6
startNum = int(input("Enter the number of slices of pizza you started with: "))
endNum = int(input("How many slices have you eaten? "))
sliceLeft = startNum - endNum
print("You have", sliceLeft, "slices remaining.")

# Ch 7
name = input("What is your name? ")
age = int(input("How old are you? "))
newAge = age+1
print(name, "next birthday you will be", newAge)

# Ch 8
bill = int(input("What is the total cost of the bill? "))
people = int(input("How many people are there? "))
each = bill/people
print("Each person should pay $", each)

# Ch 9
days = int(input("Enter the number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In", days, "days there are...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

# Ch 10
kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is", pound, "pounds")

# Ch 11
larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger // smaller
print(smaller, "goes into", larger, answer, "times")
