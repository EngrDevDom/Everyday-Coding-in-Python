# Numeric Arrays

# Ch 88
from array import *

nums = array('i', [])
for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)
nums.reverse()

print(nums)

# Ch 89
from array import *
import random

nums = array('i', [])

for i in range(0,5):
    num = random.randint(1,100)
    nums.append(num)

for i in nums:
    print(i)

# Ch 90
from array import *

nums = array('i', [])

while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
    else:
        print("Outside the range.")

for i in nums:
    print(i)

# Ch 91
from array import *

nums = array('i', [5,7,9,2,9])

for i in nums:
    print(i)

num = int(input("Enter a number: "))
if nums.count(num) == 1:
    print(num, "is in the list once.")
else:
    print(num, "is in the list", nums.count(num), "times.")

# Ch 92
from array import *
import random

num1 = array('i',[])
num2 = array('i',[])

for i in range(0,3):
    num = int(input("Enter a number: "))
    num1.append(num)

for i in range(0,5):
    num = random.randint(1,100)
    num2.append(num)

num1.extend(num2)
num1 = sorted(num1)

for i in num1:
    print(i)

# Ch 93
from array import *

nums = array('i',[])

for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array('i',[])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array.")

# Ch 94
from array import *

nums = array('i', [4,6,8,2,5])

for i in nums:
    print(i)

num = int(input("Select one of the numbers: "))

try_again = True
while try_again == True:
    if num in nums:
        print("This is in position", nums.index(num))
        try_again = False
    else:
        print("Not in array")
        num = int(input("Select one of the numbers: "))

# Ch 95
from array import *
import math

nums = array('f', [34.75,27.23,99.58,45.26,28.65])
try_again = True
while try_again == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect value, try again.")
    else:
        try_again = False

for i in range(0,5):
    ans = nums[i]/num
    print(round(ans,2))


