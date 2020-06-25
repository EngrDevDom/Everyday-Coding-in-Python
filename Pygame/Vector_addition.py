# File  :   Vector_addition
# Desc  :   Adding the __add__ Method to Our Vector Class

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

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    # rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

A = (10.0, 20.0)
B = (30.0, 35.0)
C = (15.0, 45.0)

AB = Vector.from_points(A, B)
BC = Vector.from_points(B, C)
AC = Vector.from_points(A, C)

print("Vector AC is", AC)

# Adding Vectors
AC = AB + BC
print("AB + BC is", AC)

# Calculating positions
step = AB * .1
position = Vector(*A)
for n in range(10):
    position += step
    print(position)