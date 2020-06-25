# File  :   pde_discriminant.py
# Desc  :   This program identifies the type of a Partial Differential
#           Equation is using its discriminant.

def main():

    print("This program identifies the type of a Partial Differential Equation "
          "is using its discriminant.\n")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discrim = b**2 - 4*a*c

    if discrim == 0:
        type = "Parabolic"
    elif discrim == 1:
        type = "Circular"
    elif discrim <= 0:
        type = "Elliptic"
    elif discrim >= 0:
        type = "Hyperbolic"

    print("\nDiscriminant is:", discrim)
    print("The type of equation is:", type)

main()
