# Show a Histogram

from matplotlib import pyplot as plt

population_ages = [22, 12, 55, 33, 66, 42, 15, 36, 45, 68, 69, 54, 63, 24, 25, 65, 90, 98, 65, 78, 89, 100]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.legend()
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.title('HISTOGRAM')

plt.show()

