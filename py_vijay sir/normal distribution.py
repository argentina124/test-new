# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 11:18:19 2022

@author: dhpcap
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
x=np.arange(-3,3,0.001)
plt.plot(x,norm.pdf (x,0,1))

#2) multiple normal distribution
plt.plot(x,norm.pdf(x, 0, 1), label='mu:0,sg:1')
plt.plot(x,norm.pdf(x, 0, 1.5), label='mu:0,sg:1.5')
plt.plot(x,norm.pdf(x, 0, 2), label='mu:0,sg:2')
plt.legend()

from scipy.stats import poisson
poisson.pmf(k=5,mu=3)
poisson.cdf(k=4,mu=7)


# correlation 

import pandas as pd
import seaborn as sns
data={'A':[4,5,5,6,7,8,8],
      'B':[12,14,13,7,8,9,13],
      'C':[22,24,26,29,32,20,14]}
df=pd.DataFrame(data,columns=['A','B','C'])
df.corr()

df.corr().round(3)
corr=df.corr()

sns.heatmap(corr, cmap="YlGnBu",linewidths=0.1)


import pandas as pd
import seaborn as sns
data={'A':[4,5,5,6,7,8,8],
      'B':[12,14,13,7,8,9,13],
      'C':[22,24,26,29,32,20,14]}
df=pd.DataFrame(data,columns=['A','B','C'])
df['D']=df.A*0.5
df.corr()

df.corr().round(3)
corr=df.corr()

sns.heatmap(corr,linewidths=0.1)



#outliers
import numpy as np
import scipy.stats as stats
data = np.array([14,19,20,22,24,26,27,30,30,31,36,38,44,47,99])
q3,q1=np.quantile(data, [0.75,0.25])
iqr=q3-q1
z=np.abs(stats.zscore(data))
data_clean=data[(z<3)]
data_clean


import numpy as np
import scipy.stats as stats
data = np.array([14,19,20,22,24,26,27,30,30,31,36,38,44,47,99])
q3,q1=np.quantile(data, [0.75,0.25])
iqr=q3-q1
z=np.abs(stats.zscore(data))
data_clean1=data[(abs(z)>=3)]
data_clean1

import numpy as np
import scipy.stats as stats
data = np.array([14,19,20,22,24,26,27,30,30,31,36,38,44,47,99])
q3,q1=np.quantile(data, [0.75,0.25])
iqr=q3-q1
z=np.abs(stats.zscore(data))
data_clean2=data[(abs(z)<=3)]
data_clean2

import pandas as pd
df = pd.DataFrame({'hours':[1,2,4,5,5,6,6,7,8,10,11,11,12,12,14],
'score':[64,66,76,73,74,81,83,82,80,88,84,82,91,93,89]})
import matplotlib.pyplot as plt
plt.scatter(df.hours,df.score)
plt.title('Hours studied vs. Exam Score')
plt.xlabel('Hours');
plt.ylabel('Score') ; 
plt.show()
df.boxplot(column=['score'])

import statsmodels.api as sm
y=df['score']
x=df[['hours']]
x=sm.add_constant(x)
model=sm.OLS(y,x).fit()
print(model.summary())

print("Linear Regression equation :"+ str(model.conf_int()[0][0]) + " +" + str(model.conf_int()[0][1]) + "hours")



import pandas as pd
df = pd.DataFrame({'hours':[1,2,4,5,5,6,6,7,8,10,11,11,12,12,14,90,100],
'score':[64,66,76,73,74,81,83,82,80,88,84,82,91,93,89,5,6]})
import matplotlib.pyplot as plt
plt.scatter(df.hours,df.score)
plt.title('Hours studied vs. Exam Score')
plt.xlabel('Hours');
plt.ylabel('Score') ; 
plt.show()
df.boxplot(column=['score'])

import statsmodels.api as sm
y=df['score']
x=df[['hours']]
x=sm.add_constant(x)
model=sm.OLS(y,x).fit()
print(model.summary())

print("Linear Regression equation :"+ str(model.conf_int()[0][0]) + " +" + str(model.conf_int()[0][1]) + "hours")





















