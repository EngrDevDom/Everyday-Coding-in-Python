from scipy import *
"""
   Finds all solutions of the equation Integrate[j1(t)/t,{t,0,x}] == 1
   in the range x = [0, 100]
"""

def func(x, a):
      """ Computes Integrate [j1(t)/t,{t,0,x}] - a """
      return integrate.quad(lambda t: special.j1(t)/t, 0, x)[0] - a

# Finds approximate solutions of the equation in the range[0:100]
x = r_[0:100:0.2]                   # creates an equally spaced array
b = map(lambda t: func(t, 1), x)    # evaluates function on this array

z = [];                             # approximate solutions of the equation
for i in range(1, len(b)):                # if the function changes sign,
      if (b[i-1]*b[i]<0): z. append(x[i]) # the solution os bracketed

print("Zeroes of the equation in the intercal [0:100] are")
j = 0
for zt in z:
      print(j, optimize.fsolve(func, zt, (1,))  # calling root finding routine, finds all zeros
      j=j+1
