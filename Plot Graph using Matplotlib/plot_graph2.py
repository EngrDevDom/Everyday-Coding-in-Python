import matplotlib.pyplot as plt
import numpy as np

x = np.linspae(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubic')

# Add an x-label to the axes.
ax.set_xlabel('x label')

# Add a y-label to the axes.
ax.set_ylabel('y label')

# Add a title to the axes.
ax.set_title("Simple Plot")
ax.legend()

plt.show()
