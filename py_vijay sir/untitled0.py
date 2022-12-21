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
    print(random.randint(0,10),end="\t")