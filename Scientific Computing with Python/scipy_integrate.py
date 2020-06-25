# scipy integrate example

from scipy import *
import scipy

def func(x):
      return integrate.quad(cos, 0, x)[0]

vecfunc = vectorize(func)

x = r_[0:2*pi:100j]
x2 = x[::5]
y = sin(x)
y2 = vecfunc(x2)

xplt.plot(x, y, x2, y2, 'rx')
