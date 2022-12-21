# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:31:53 2022

@author: dhpcap
"""
#1)
import numpy as np
i=np.array([[1, 2, 3], [2, 7, 8]])

j=np.array([[1, 3],
   [9,8],
   [2, 6]])

z=i@j
z

#2)

#a)

a=np.array([[1,6,9],
           [0,3,3],
           [8,2,5]])

a[[0, 1]] = a[[1, 0]]
a

#b)

a[0] = a[0]*5
a

#c)

a[0] = a[0]-a[2]
print("subtract row R1-->R1-R2")
print(a)