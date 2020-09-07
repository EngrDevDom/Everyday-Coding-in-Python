# Show Bar Graph

from matplotlib import pyplot as plt

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="One")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Two", color='b')

plt.legend()
plt.xlabel('Number')
plt.ylabel('Height')
plt.title('Info')

plt.show()

