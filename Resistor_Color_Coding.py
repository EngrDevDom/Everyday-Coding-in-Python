'''
    Resistor Color Coding
    - This program calculates the value of a resistor based on the colors
    entered by the user.
'''

# Initialize the values
black = 0
brown = 1
red = 2
orange = 3
yellow = 4
green = 5
blue = 6
violet = 7
grey = 8
white = 9
gold = 0
silver = 0

bands = input('Enter the color bands: ')
code = bands.split(" ")

print('1st Band\t', '2nd Band\t', 'Multiplier\t', 'Tolerance\t', 'Reliability')
print(code[0], '\t\t', code[1], '\t\t', code[2], '\t\t', code[3], '\t\t', code[4])

