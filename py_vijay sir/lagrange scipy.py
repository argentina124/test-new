# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:28:33 2022

@author: dhpcap
"""



import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
from scipy.interpolate import lagrange



x = [0, 1, 2]
y = [1, 3, 2]

f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()