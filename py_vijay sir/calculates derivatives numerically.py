# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:18:33 2022

@author: dhpcap
"""

''' Consider the function f(x)=cos(x). 
We know the derivative of cos(x) is −sin(x). 
Although in practice we may not know the underlying 
function we are finding the derivative for, 
we use the simple example to illustrate the aforementioned 
numerical differentiation methods and their accuracy. 
The following code computes the derivatives numerically.
'''

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')


# step size
h = 0.1
# define grid
x = np.arange(0, 2*np.pi, h) 
# compute function
y = np.cos(x) 

# compute vector of forward differences
forward_diff = np.diff(y)/h 
# compute corresponding grid
x_diff = x[:-1:] 
# compute exact solution
exact_solution = -np.sin(x_diff) 

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x_diff, forward_diff, '--', \
         label = 'Finite difference approximation')
plt.plot(x_diff, exact_solution, \
         label = 'Exact solution')
plt.legend()
plt.show()

# Compute max error between 
# numerical derivative and exact solution
max_error = max(abs(exact_solution - forward_diff))
print(max_error)