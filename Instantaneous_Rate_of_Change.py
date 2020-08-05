from sympy import Symbol, Limit, delta
t = Symbol('t')
St = 5*t**2 + 2*t + 8

t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St1 = St.subs({t: t1})
St1.delta = St.subs({t: t1 + delta_t})

