from matplotlib import pyplot as plt
import numpy as np
import math

x = np.arange(0, math.PI*2, 0.05)
y = np.tan(x)

plt.plot(x, y)
plt.xlabel("angle")
plt.ylabel("Tan value")
plt.title('Tan wave')
plt.show()
