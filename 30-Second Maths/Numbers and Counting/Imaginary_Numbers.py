import math

real_num1 = int(input('Enter the 1st real number part: '))
real_num2 = int(input('Enter the 2nd real number part: '))

# Complex Number
print('Complex Number:', real_num1, '+', real_num2, 'i')

# Polar Coordinates
rad = math.sqrt(real_num1**2 + real_num2**2)
theta = math.atan(real_num2/real_num1)

print('Polar Coordinates:', rad, '<', theta)

