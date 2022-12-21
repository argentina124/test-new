# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:09:59 2022

@author: dhpcap
"""

import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt 
M = [[1, 1, 1, 1], [1, 2, 4, 2**3], [1, 3, 9, 27], [1, 3.4, 3.4**2, 3.4**3]] 
yv = [1.1, 2.1, 5, 7] 
a = np.matmul(np.linalg.inv(M),yv) 
x = sp.symbols('x') 
y = a[0] + a[1]*x + a[2]*x**2 + a[3]*x**3 # Creating an equation
x_val = np.arange(0,4,0.01) 
plt.plot(x_val, [y.subs(x,i) for i in x_val]) # subs=Substitute
plt.scatter([1, 2, 3, 3.4],[1.1, 2.1, 5, 7], c='k') 
plt.title(sp.N(y,5)) 
plt.grid(); 
plt.show()