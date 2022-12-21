# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:01:23 2022

@author: dhpcap
"""

# Program a function my_bisection(f, a, b, tol) 
# that approximates a root r of f, 
# bounded by a and b to within |f(a+b2)|<tol

import numpy as np

def my_bisection(f, a, b, tol): 
    # approximates a root, R, of f bounded 
    # by a and b to within tolerance 
    # | f(m) | < tol with m the midpoint 
    # between a and b Recursive implementation
    
    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "The scalars a and b do not bound a root")
        
    # get midpoint
    m = (a + b)/2
    
    if np.abs(f(m)) < tol:
        # stopping condition, report m as root
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return my_bisection(f, a, m, tol)
    
# The 2–√ can be computed as the root of the function f(x)=x2−2.
# Starting at a=0 and b=2,
# use my_bisection to approximate the 2–√ to a 
# tolerance of |f(x)|<0.1 and |f(x)|<0.01. 
# Verify that the results are close to a root 
# by plugging the root back into the function
    
f = lambda x: x**2 - 2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)

print("f(r1) =", f(r1))
print("f(r01) =", f(r01))

f = lambda x: x**2 - 2

r1 = my_bisection(f, 2, 4, 0.01)
print("r1 =", r1)
r01 = my_bisection(f, 2, 4, 0.01)
print("r01 =", r01)

print("f(r1) =", f(r1))
print("f(r01) =", f(r01))