'''
    Finding the Limit of Functions
'''

from sympy import Limit, Symbol, S

# Unevaluated
x = Symbol('x')

# Find the value of the limit
l = Limit(1/x, x, S.Infinity)
print(Limit(1/x, x, S.Infinity), '=', l.doit())

