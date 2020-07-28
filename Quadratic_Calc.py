'''
    Quadratic function calculator
'''

# Assume values of x
x_values = [ -1, 1, 2, 3, 4, 5]

for x in x_values:
    # Calculate the value of quadratic function
    y = x**2 + 2*x + 1
    print('x = {0}, y = {1}'.format(x, y))

