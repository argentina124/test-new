# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:30:24 2022

@author: dhpcap
"""


## Use the trapz function to approximate ∫π0sin(x)dx for 11 
# equally spaced points over the whole interval. 
# Compare this value to the one computed in the early example 
# using the Trapezoid Rule

import numpy as np
from scipy.integrate import trapz

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_trapz = trapz(f,x)
I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1]) + f[n-1])

print(I_trapz)
print(I_trap)


# Use the cumtrapz function to approximate the cumulative integral 
# of f(x)=sin(x) from 0 to π with a discretization step of 0.01.
# The exact solution of this integral is F(x)=sin(x). 
# Plot the results.

from scipy.integrate import cumtrapz
import matplotlib.pyplot as plt


plt.style.use('seaborn-poster')

x = np.arange(0, np.pi, 0.01)
F_exact = -np.cos(x)
F_approx = cumtrapz(np.sin(x), x)

plt.figure(figsize = (10,6))
plt.plot(x, F_exact)
plt.plot(x[1::], F_approx)
plt.grid()
plt.tight_layout()
plt.title('$F(x) = \int_0^{x} sin(y) dy$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['Exact with Offset', 'Approx'])
plt.show()

## Use the integrate.quad function to compute ∫π0sin(x)dx. 
## Compare your answer with the correct answer of 2

from scipy.integrate import quad 

I_quad, est_err_quad = \
          quad(np.sin, 0, np.pi)
print(I_quad)
err_quad = 2 - I_quad
print(est_err_quad, err_quad)

