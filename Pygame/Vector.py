# File  :   Vector.py
# Desc  :   Creating Vectors from points

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def from_points(P1, P2):
        return Vector(P2[0] - P1[0], P2[1] - P1[1])

A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector.from_points(A, B)

print(AB)