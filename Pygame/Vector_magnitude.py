# File  :   Vector_magnitude.py
# Desc  :   Creating a Vector and show its magnitude function

import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def from_points(P1, P2):
        return Vector(P2[0] - P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector.from_points(A, B)

print(AB)
print(AB.get_magnitude())