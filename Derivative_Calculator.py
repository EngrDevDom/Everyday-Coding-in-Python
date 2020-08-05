'''
    Derivative Calculator
        -> A key assumption in this is that all the functions to be calculated,
        the derivative of are differentiable in their respective domains.
'''

from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()       # Define a function(f) and a variable(var) to differentiate
    pprint(d)

if __name__ == '__main__':
    f = input('Enter a function: ')
    var = input('Enter the variable to differentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid input')
    else:
        derivative(f, var)

