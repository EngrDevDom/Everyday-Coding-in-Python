'''
    Finding the Integrals of the Functions
'''

# Indefinite Integral
from sympy import Integral, Symbol
x = Symbol('x')
k = Symbol('k')
print('Integral(k*x, x) =', Integral(k*x, x).doit())


# f = kx at limits [0, 2]
print('Integral(k*x, (x, 0, 2) =', Integral(k*x, (x, 0, 2)).doit())

# f = x at limits [2, 4]
print('Integral(x, (x, 2, 4)) =', Integral(x, (x, 2, 4)).doit())

