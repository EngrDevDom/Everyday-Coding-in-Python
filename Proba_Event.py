'''
    Probability Events
'''

from sympy import FiniteSet

# A = The number is prime
# B = The number is odd

# Probability of Event A or Event B
s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.union(b)
len(e)/len(s)       # 0.666666666...


# Probability of Event A and Event B
s = FinitSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.intersect(b)
len(e)/len(s)       # 0.333333333...

