# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:56:49 2022

@author: dhpcap
"""

# Using fsolve function from scipy 
# to compute the root of f(x)=cos(x)−x near −2. 
# Verify that the solution is a root (or close enough).

import numpy as np
from scipy import optimize

f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)
print("r =", r)

# Verify the solution is a root
result = f(r)
print("result=", result)

# The function f(x)=1x has no root. 
# Use the fsolve function to try to compute the root of f(x)=1x. 
# Turn on the full_output to see what’s going on

f = lambda x: 1/x

r, infodict, ier, mesg = optimize.fsolve(f, -2, full_output=True)
print("r =", r)

result = f(r)
print("result=", result)

print(mesg)