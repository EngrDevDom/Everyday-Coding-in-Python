from sympy import Symbol, Derivative

x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)
print(Derivative(f, x).doit())      # Executing -> Product Rule

