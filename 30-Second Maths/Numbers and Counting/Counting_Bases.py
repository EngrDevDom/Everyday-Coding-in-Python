import math

num = int(input('Enter a number: '))
base = int(input('Enter the base: '))

if base == 10:
    value = num

elif base == 2:
    value = num%2

print(num, 'to the base of', base, 'is equal to', value)

