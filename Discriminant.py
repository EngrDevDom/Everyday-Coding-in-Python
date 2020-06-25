# This program calculates the discriminant or
# the roots of a given quadratic equation.

import math

a, b, c, = map(float, input("Input the coefficients a!=0 : ")).split()
x1 = x2 = 0
D = b*b-4*a*c
denominator = 2*a

if D == 0:
    x = -b/denominator
    print("The value of x1 and x2 is the same and it is equal to: ", x)
elif D > 0:
    x1 = (-b+math.sqrt(D))/denominator
    x2 = (-b-math.sqrt(D))/denominator
    print("The value of x1 is : ", x1)
    print("The value of x2 is : ", x2)
else:
    D *= -1
    D = math.sqrt(D)
    print("The value of x1 is : (", -b, "+i", D, ")/", denominator)
    print("The value of x1 is : (", -b, "-i", D, ")/", denominator)