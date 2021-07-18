from scipy.optimize import root, minimize
from math import cos 

def eqn(x):
    return x + cos(x)

def eqn2(x):
    return x**2 + x + 2

myroot = root(eqn, 0)
mymin = minimize(eqn2, 0, method='BFGS')
print(mymin)