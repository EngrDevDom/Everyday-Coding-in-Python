import matplotlib.pyplot as plt

a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
a3 = plt.subplot2grid((3,3),(1,0),rowspan = 2, colspan = 2)

import numpy as np

x = np.arange(1,10)

a2.plot(x, x*x,'r')
a2.set_title('square')
a1.plot(x, np.exp(x),'b')
a1.set_title('exp')
a3.plot(x, np.log(x),'g')
a3.set_title('log')

plt.tight_layout()
plt.show()