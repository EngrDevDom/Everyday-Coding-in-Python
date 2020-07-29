'''
    Math -> Sets
'''

from sympy import FiniteSet

# Set Construction
s = FiniteSet(2, 4, 6)
len(s)      # 3

# Check whether a number is in the set
4 in s  # False

# Empty Set
s = FiniteSet()     # EmptySet()

# Set Repetition and Order
members = [1, 2, 3, 2]
FiniteSet(*members)     # {1, 2, 3}
for member in s:
    print(member)       # 1, 2, 3

# Subsets -> if all the members of s are also a member of t
s = FiniteSet(1)
t = FiniteSet(1,2)
s.is_subset(t)      # True
t.is_subset(s)      # False

# Supersets -> if t contains all of the members contained in s
s.is_superset(t)    # True
t.is_superset(s)    # True

# Powerset -> is the set of all possible subsets of s
s = FiniteSet(1, 2, 3)
ps = s.powerset()
ps                  # {{1}, {1, 2}, {1, 3}, {1, 2, 3}, {2}, {2, 3}, {3}, EmptySet()}

len(ps)             # 8

# Proper subset -> if all the members of s are also in t and t has at least one member that is not in s
s = FiniteSet(1, 2, 3)
t = FiniteSet(1, 2, 3)
s.is_proper_subset(t)       # False
t.is_proper_subset(s)       # False

t = FiniteSet(1, 2, 3, 4)
s.is_proper_subset(t)       # True
t.is_proper_subset(s)       # True

