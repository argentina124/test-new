# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 09:03:08 2022

@author: dhpcap
"""

data=[9,9,9,8,8,8,8,7,7,7,7,7,6,6,6,6,5,5]
mean = sum(data) / len(data)
deviation_from_Mean = sum((v-mean) for v in data)
squared_deviation= sum((v - mean) ** 2 for v in data)
variance = sum((v-mean) ** 2 for v in data)/ len (data)
standard_deviation=variance**0.5

print("Mean :", mean)
print("Deviation_from_Mean :", deviation_from_Mean)
print("Squared_Deviation :, squared_deviation")
print("variance :", variance)
print("standard_deviation :", standard_deviation)

####################################

import numpy as np
data=[9,9,9,8,8,8,8,7,7,7,7,7,6,6,6,6,5,5]
print("Mean : ", np.mean(data))
print("variance : ",np.var(data))
print ("standard_deviation :", np.std(data))