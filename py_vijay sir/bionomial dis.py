# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:17:39 2022

@author: dhpcap
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x=random.binomial(n=2, p=0.5, size=1000)
sns.histplot(x)
plt.show()
