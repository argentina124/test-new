# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:32:50 2022

@author: dhpcap
"""

import numpy as np
def IT(f,a,b,n):
    h=(b-a)/n
    sum=0
    for i in range (int(n)):
        t=(f(a+i*h) + f(a+(i+1)*h))*h/2
        sum = sum+t
    return sum
def f(x):
    y=2+2*x+x**2+np.sin(2*np.pi*x)+np.cos(2*np.pi*x/0.5)
    return y
print(IT(f,0,1.5,1.0))
print(IT(f,0,1.5,9.0))
