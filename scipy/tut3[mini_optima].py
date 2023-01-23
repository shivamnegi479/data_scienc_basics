from scipy.optimize import root
from scipy.optimize import minimize
from math import cos

# def eq(x):
#     return x**2
# def eq(x):
#     return x+cos(x)

# myrott=root(eq,0)
# print(myrott.x)

def mini(x):
    return x**2 +x+2

ans=minimize(mini,0,method="BFGS")
print(ans.x)

