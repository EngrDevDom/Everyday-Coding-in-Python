# Import required modules/ libraries
import numpy as np
from scipy import linalg

# We are trying to solve a linear algebra system which can be given as:
#               1x + 2y =5
#               3x + 4y =6

# Create input array
A= np.array([[1,2],[3,4]])

# Solution Array
B= np.array([[5],[6]])

# Solve the linear algebra
X= linalg.solve(A,B)

# Print results
print(X)

# Checking Results
print("\n Checking results, following vector should be all zeros")
print(A.dot(X)-B)