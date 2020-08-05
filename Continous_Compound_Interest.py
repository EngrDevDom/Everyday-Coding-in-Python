from sympy import Limit, Symbol, S

p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
n = Symbol('n', positive=True)
print(Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit())

