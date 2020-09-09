from numpy import poly1d

# We'll use some functions from numpy remember!!
# Creating a simple polynomial object using coefficients
somePolynomial = poly1d([1,2,3])

# Printing the result
# Notice how easy it is to read the polynomial this way
print(somePolynomial)

# Let's perform some manipulations
print("\nSquaring the polynomial: \n")
print(somePolynomial*somePolynomial)

# How about integration, we just have to call a function
# We just have to pass a constant say 3
print("\nIntegrating the polynomial: \n")
print(somePolynomial.integ(k=3))

# We can also find derivatives in similar way
print("\nFinding derivative of the polynomial: \n")
print(somePolynomial.deriv())

# We can also solve the polynomial for some value,
# let's try to solve it for 2
print("\nSolving the polynomial for 2: \n")
print(somePolynomial(2))
