# Fraction_Calc.py

''' Fraction Operations '''
from fractions import Fraction

def add(a,b):
    print('Result of Addition: {0}'.format(a+b))

def subtract(a,b):
    print('Result of Subtraction: {0}'.format(a-b))

def multiply(a,b):
    print('Result of Multiplication: {0}'.format(a*b))

def divide(a, b):
    print('Result of Division: {0}'.format(a/b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - Add, Subtract, Multiply, Divide: ')
    if op == 'Add':
        add(a,b)
    elif op == 'Subtract':
        subtract(a,b)
    elif op == 'Multiply':
        multiply(a,b)
    elif op == 'Divide':
        divide(a,b)
    else:
        exit()
