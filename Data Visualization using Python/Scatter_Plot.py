# Show a Scatter Plot

from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 2, 3, 4, 6, 8, 2, 4, 3]

plt.scatter(x, y, label='Scatter Plot')
plt.legend()
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('Scatter')

plt.show()

