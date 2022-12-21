# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:55:25 2022

@author: dhpcap
"""

import numpy as np 
import pandas as pd
def f(x): return np.sin(5*x) + np.cos(2*x)
def bisec2 (f,a,b):
    xi = (a+b)/2
    if f(a)*f(b):return [xi, a,b, "Root Not Bracketed"]
    elif f(xi) == 0: return [xi,a,b, "Root Found"]
    elif f(xi)*f(a) < 0: return [xi,a,xi, "Root between a and xi"]
    elif f(xi)*f(b) < 0: return [xi,xi,b, "Root between xi and b"]
    
def bisection(ErrorTable,ErrorNotTable,atable,btable,xtable):
  MaxIter = 20
  eps = 0.0005
  Stopcode = "NoStoping"
  i = 0
  while i <= MaxIter and Stopcode == "NotStoping":
      ri=bisec2(f,atable[i] , btable[i])
      if ri[3] == "Root Not Bracketed":
          xtable.append(ri [0])
          ErrorNotTable.append(ri[3])
          break
      if ri[3] == "Root Found":
          xtable.append(ri[0])
          ErrorTable.append(0)
          ErrorNotTable.append(ri[3])
          break
      atable.append(ri[1])
      btable.append(ri[2])
      xtable.append(ri[0])
      ErrorNotTable.append(ri[3])
      if  i !=0:
          ei (xtable[i]-xtable[i-1])/xtable[i]
          ErrorNotTable.append(ei)
      if abs(ErrorTable[i])> eps:
         Stopcode = "NotStopping"
      else:
         stopcode = "Stop"
         i+=1
         T2= ([[i,table[i],btable[i],xtable[i],f(atable[i]),
               f(btable[i]), f(xtable[i]), ErrorTable[i],
               ErrorNotTable[i]] for i in range(len(xtable))])
         T2 = pd.DataFrame()(T2,colums=["Iteration","a","b","c","x_i","f[a]","f[b]","f[x_i]", "er","ErrorNote"])
         display(T2)
        
# First root
ErrorTable = [1]
ErrorNotTable = [1]
atable = [-6.6]
btable = [-0.5]
xtable = []
print ("First Root")
bisection(ErrorTable, ErrorNotTable, atable, btable, xtable)

#second root
ErrorTable = [1]
ErrorNotTable = []
atable = [-0.3]
btable = [-0.2]
xtable = []
print ("Second Root")
bisection(ErrorTable, ErrorNotTable, atable, btable, xtable)
 
#Third Root
ErrorTable = [1]
ErrorNotTable = []
atable = [0.1]
btable = [0.9]
xtable = []
print ("Third Root")
bisection(ErrorTable, ErrorNotTable, atable, btable, xtable)
         
          
          
 
    