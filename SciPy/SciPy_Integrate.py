# Import required packages
from scipy import integrate

# Using quad as we can see in list quad is used for simple integration
# arg1: A lambda function which returns x squared for every x
# We'll be integrating this function
# arg2: lower limit
# arg3: upper limit
result= integrate.quad(lambda x: x**2, 0,3)
print(result)