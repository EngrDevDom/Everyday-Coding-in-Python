'''
    Finding the Derivative of Functions
'''

from sympy import Symbol, Derivative

t = Symbol('t')
St = 5*t**2 + 2*t + 8

# Find the value of the Derivative
d = Derivative(St, t)
print(Derivative(St, t), '=', d.doit())

# Substitute a value
print(d.doit().subs({t:1}))

