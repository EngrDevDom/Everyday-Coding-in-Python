# Style in Graph

from matplotlib import pyplot as plt
from matplotlib import style

x = [5, 8, 9]
y = [15, 18, 6]
x2 = [6, 9, 10]
y2 = [6, 18, 16]

plt.plot(x, y, 'g', label="Line One", linewidth=4)
plt.plot(x2, y2, 'b', label="Line Two", linewidth=4)

plt.title("Information")
plt.ylabel("Y AXIS")
plt.xlabel("X AXIS")

plt.legend()
plt.grid(True, color='k')
plt.show()

