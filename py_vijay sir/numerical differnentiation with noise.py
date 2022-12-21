# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:29:03 2022

@author: dhpcap
"""

'''we numerically compute the derivative of a 
simple cosine wave corrupted by a small sin wave

To illustrate this point, 
we plot fϵ,ω(x) for ϵ=0.01 and ω=100, 
and we can see it is very close to f(x), 
as shown in the following figure.
'''

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')


x = np.arange(0, 2*np.pi, 0.01) 
# compute function
omega = 100
epsilon = 0.01

y = np.cos(x) 
y_noise = y + epsilon*np.sin(omega*x)

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x, y_noise, 'r-', \
         label = 'cos(x) + noise')
plt.plot(x, y, 'b-', \
         label = 'cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()


##  the following figure shows f′(x) and f′ϵ,ω(x) 
##  for ϵ=0.01 and ω=100.

x = np.arange(0, 2*np.pi, 0.01) 
# compute function
y = -np.sin(x) 
y_noise = y + epsilon*omega*np.cos(omega*x)

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x, y_noise, 'r-', \
         label = 'Derivative cos(x) + noise')
plt.plot(x, y, 'b-', \
         label = 'Derivative of cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()

