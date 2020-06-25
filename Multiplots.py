import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, math.pi*2, 0.05)
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
axes3 = fig.add_axes([0.2, 0.3, 0.2, 0.3]) # inset axes

axes1.plot(x, np.sin(x), 'b')
axes2.plot(x,np.cos(x),'r')
axes3.plot(x,np.tan(x),'g')

axes1.set_title('sine')
axes2.set_title("cosine")
axes3.set_title("tangent")

plt.show()