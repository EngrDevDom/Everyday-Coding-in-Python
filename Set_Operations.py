'''
    Math -> Set Operations
'''

from sympy import FiniteSet

# Union
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
s.union(t)              # {1, 2, 3, 4, 6,}

# Union of three Sets
s = FiniteSet(1, 2, 3)
t = FiniteSet(2, 4, 6)
u = FiniteSet(3, 5, 7)
s.union(t).union(u)     # {1, 2, 3, 4, 5, 6, 7}

# Intersection
s = FiniteSet(1, 2)
t = FiniteSet(2, 3)
s.intersect(t)          # 2

# Intersection of three Sets
s.intersect(t).interset(u)      # EmpySet()

# Cartesian Product
s = FiniteSet(1, 2)
t = FiniteSet(3, 4)
p = s*t
p                       # {1, 2} x {3, 4}
for elem in p:
    print(elem)         # (1, 3), (1,4), (2, 3), (2, 4)

# Cardinality of the Cartesian Product
len(p) == len(s)*len(t)     # True

