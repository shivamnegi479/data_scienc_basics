# Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

from scipy.optimize import root
from math import sin
from math import cos

def eq(x):
    return x+cos(x)
x1=12
myr=root(eq,30)
print(myr.x)




