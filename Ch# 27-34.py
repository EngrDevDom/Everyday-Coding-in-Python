# Ch 27
num = float(input("Enter a numbers with lots of decimal places: "))
print("The answer is", (num*2))

# Ch 28
num = float(input("Enter a numbers with lots of decimal places: "))
print("The answer is", round(num*2, 2))

# Ch 29
import math

num = float(input("Enter a number over 500: "))
print("The answer is", round(math.sqrt(num), 2))

# Ch 30
import math

print("Value of pi =", round(math.pi, 5))

# Ch 31
import math

radius = float(input("Enter the radius of the circle: "))
Area = math.pi * radius**2
print("The Area of Circle is", Area)

# Ch 32
import math

radius = float(input("Enter the radius of cylinder: "))
depth = float(input("Enter the depth of cylinder: "))
Area = (math.pi * radius**2) * depth
print("The Area of Cylinder is", round(Area, 3))

# Ch 33
num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number: "))
whole = num1//num2
remainder = num1%num2
print(num1, "divided by", num2, "is", whole, "with", remainder, "remaining.")

# Ch 34
choice = input("1. Square\n2. Triangle\nEnter a number: ")
if choice == "1":
    length = float(input("Enter the length of one side: "))
    Area = length**2
    print("\nThe Area is", round(Area, 2))
elif choice == "2":
    base = float(input("Enter the value of base: "))
    height = float(input("Enter the value of height: "))
    Area = (base * height)/2
    print("\nThe Area is", round(Area, 2))
else:
    input("\nError message! Press <Enter> and try again.")
