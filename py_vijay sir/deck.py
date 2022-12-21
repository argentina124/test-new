# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:23:20 2022

@author: dhpcap
"""

import numpy as np

from numpy.random import rand 

org_deck=[
      '1S','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS'
      '1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QQ','KH'
      '1C','2C','3C','4C','5C','6C','7c','8C','9C','10C','JC','QC','KC'
      '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD'  
       ]
def MonteCarlo(number_of_sample):
          count=0
          for i in deck:
            if deck[i][1]=='k' and deck[i+1][1]=='k'
            np.random.shuffle(deck)
            if kingking(deck):
                count=count+1
                
                
            
           

