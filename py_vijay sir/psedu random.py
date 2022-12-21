# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 08:54:02 2022

@author: dhpcap
"""

import random 
from datetime import datetime
dt=datetime.now()
random.seed(int(dt.strftime('%Y%m%d%H%M%S%f')))
for i in range(5):
    print(random.randint(0,100),end="\t")


##fix seed     
import random 
from datetime import datetime
dt=datetime.now()
random.seed(10)
for i in range(5):
    print(random.randint(0,100),end="\t")  
    
    
##parallel random number generation

from numpy.random import SeedSequence,default_rng
ss=SeedSequence(12345)
child_seeds=ss.spawn(10)
streams=[default_rng(s) for s in child_seeds]
grandchildren=child_seeds[0].spawn(4)
grand_streams=[default_rng(s) for s in grandchildren]
grand_streams
child_seeds


##mean and std derivation

import numpy as np
import matplotlib.pyplot as plt
mu,sigma=0,0.1
s=np.random.normal(mu,sigma,1000)
plt.hist(s,blns=25,density=False,alpha=0.6)
plt.show()


##################
import numpy as np
s=np.random.triangular(-3,0,8,100000)
plt.hist(s,blns=25,density=False,alpha=0.6)
plt.show()

#############
import matplotlib.pyplot as plt
s=np.random.uniform(-1,0,1000)
count,bins,ignored=plt.hist(s,15,density=True)
plt.plot(bins,np.ones_like(bins),linewidth=2,color='r')
plt.show()


############


def f(x):
    return x^3+6*x-x+17

rn=list(np.random.randint(low=3,high=8,size=20))

xi=[]
for i in rn:
    xi.append(f(i))
    
Area=[]
for h in xi:
    Area.append(h*7)

np.mean(Area)



