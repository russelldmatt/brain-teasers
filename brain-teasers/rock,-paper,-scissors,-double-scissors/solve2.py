import numpy as np
import sympy
from sympy import *
print(sympy.__version__)
# from sympy.solvers.solveset import nonlinsolve

p, d, r = symbols('p, d, r', real = True)

expr1 = (p + d/2.)/(1-r)
expr2 = (r/2. + d)/(1-p)
expr3 = r + d
expr4 = (r + p/2.)/(1-d)
expr5 = p + d + r - 1

for solution in nsolve((expr1 - expr3, expr2 - expr3, expr4 - expr3, expr5), (p, d, r), [0.4, 0.27, 0.33], verify = False):
    print "solution:", solution

def sub(expr, solution):
    z = expr.subs(r, solution[0])
    z = z.subs(p, solution[1])
    z = z.subs(d, solution[2])
    return z

def expr_values(solution):
    return [ sub(expr1, solution), 
             sub(expr2, solution),
             sub(expr3, solution),
             sub(expr4, solution)]

solution = [ 0.4, 0.27, 0.33 ]
# solution = [0.266590844735438,
#             0.357435687058534,
#             0.356121374866432]
for z in expr_values(solution):
    print z

def f(x): # x is [r, p]
    d = 1 - sum(x)
    z = np.append(x, d)
    if min(z) < 0: return 500
    return -float(min(expr_values(z)))

x0 = [ 0.4, 0.27 ]
print "f(x):", f(x0)
x0 = [ 0.39723677,  0.27328221] # 0.32948102
print "f(x):", f(x0)

from scipy.optimize import basinhopping
print type(float(f(x0)))
print basinhopping(f, x0)

