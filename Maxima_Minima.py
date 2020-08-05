'''
    Higher Order Derivatives -> Finding the Maxima and Minima
'''

from sympy import Symbol, solve, Derivative

x = Symbol('x')
f = x**5 - 30*x**3 + 50*x

# 1st Derivative
d1 = Derivative(f, x).doit()
critical_points = solve(d1)
print(critical_points)

A = critical_points[2]
B = critical_points[0]
C = critical_points[1]
D = critical_points[3]

# 2nd Derivative
d2 = Derivative(f, x, 2).doit()

# Substitute values
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:A}).evalf())
print(d2.subs({x:D}).evalf())

# Create two labels x_min, and x_max to refer to the domain boundaries and
# evaluate the function at the points A, C, xmin and x_max.
x_min = -5
x_max = 5

print(f.subs({x:A}.evalf()))        # Global Maximum
print(f.subs({x:C}.evalf()))
print(f.subs({x:x_min}.evalf()))
print(f.subs({x:x_max}.evalf()))

print(f.subs({x:B}.evalf()))
print(f.subs({x:D}.evalf()))        # Global Minimum
print(f.subs({x:x_min}.evalf()))
print(f.subs({x:x_max}.evalf()))

