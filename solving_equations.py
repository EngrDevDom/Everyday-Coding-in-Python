'''
    Solving equations using Sympy -> One of the Equations of Motion
'''

from sympy import Symbol, solve, pprint

s = Symbol('s')     # distance
u = Symbol('u')     # initial velocity
t = Symbol('t')     # time
a = Symbol('a')     # acceleration

expr = u*t + (1/2)*a*t*t - s        # This is the equation equate to zero
t_expr = solve(expr, t, dict=True)
pprint(t_expr)

