# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:42:29 2022

@author: dhpcap
"""

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
N=10000
a,b=(50,50)
x_min,x_max=(0,.55)
randx=np.random.uniform(x_min,x_max,N)
y=stats.beta.pdf(randx,a,b)
beta_at_55=stats.beta(a,b).cdf(.55)
Mcarlo_width=x_max-x_min
Mcarlo_rect_area=Mcarlo_width*y.sum()
Mcarlo_rect_area_avg=Mcarlo_rect_area/N
print(f'Real value to find:{beta_at_55}')
print(f'Integral value: {Mcarlo_rect_area_avg}')


########

import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

def mc_normal(mean,std_dev,samples):
    results = []
    for _ in range(samples):
        results.append(rnd.normal(mean,std_dev))
    return np.array(results)

s = 100000

upper_limit = 34

component_1 = mc_normal(5,1,s)
component_2 = mc_normal(10,1,s)
component_3 = mc_normal(15,1,s)

total = component_1 + component_2 + component_3

probability = np.sum(total > upper_limit)/len(total)*100
print("probability of exceeding the time limit:",round(probability, 3), "%")

count,bins,ignored=plt.hist(total, 30 ,density=True,color='skyblue')
plt.vlines(34, count.min(), count.max(), color='r',label="34 Minute")
plt.legend();
plt.show()
    