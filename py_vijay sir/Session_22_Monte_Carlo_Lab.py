# Monte Carlo - Area under Beta distibution
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
N = 10000
a, b = (50,50) 			             # Beta function 𝛼,𝛽
x_min, x_max = (0, .55) 		                      # min max points for area to compute
randx = np.random.uniform(x_min, x_max, N) 	  # Generate random uniform generated points
y = stats.beta.pdf(randx, a, b) 		                # Generate beta Dist Fun points
beta_at_55= stats.beta(a,b).cdf(.55) 	                # beta fun area <=0.55 (orange)
Mcarlo_width= x_max-x_min 		                     # Monte-Carlo interval length
Mcarlo_rect_area= Mcarlo_width*y.sum() 	          # Monte-Carlo area of all rectangle
Mcarlo_rect_area_avg= Mcarlo_rect_area/N 	       # Monte-Carlo avg area of all rectangle
print(f'Real value to find: {beta_at_55}')
print(f'Integral value:  {Mcarlo_rect_area_avg}')


##-----------------------------------------------------------------------------
# Monte Carlo - Process Simulation
import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

def mc_normal(mean, std_dev, samples):
    results = []
    for _ in range(samples):
        results.append(rnd.normal(mean, std_dev))
    return np.array(results)

# configuration
s = 100000 # number of samples
upper_limit = 34 # upper limit from specification
# components
component_1 = mc_normal(5,1,s)
component_2 = mc_normal(10,1,s)
component_3 = mc_normal(15,1,s)
# relationships
total = component_1 + component_2 + component_3
# success conditions
probability = np.sum(total > upper_limit)/len(total)*100
print("Probability of exceeding the time limit: ", round(probability, 3), "%")

count, bins, ignored = plt.hist(total, 30, density=True,color='skyblue')
plt.vlines(34,count.min(),count.max(),color='r',label="34 Minute")
plt.legend() ; plt.show()

##-----------------------------------------------------------------------------
# Monte Carlo - Card Game - King-King combination
import numpy as np
import copy
import matplotlib.pyplot as plt
org_deck=[
    '1S','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
    '1H','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
    '1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',
    '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD'
    ]

def kingking(deck):
    for i in range(len(deck)-1):
        if deck[i][0]=='K' and deck[i+1][0]=='K':
            return True
    

def MonteCarlo(n):
    res=0.0
    for i in range(n):
        deck= copy.deepcopy(org_deck)
        np.random.shuffle(deck) #Shuffle a deck
        if kingking(deck): # check if there is King-King combination
            res=res+1
    print(res/n*100)
    return res/n*100

#Simulate
result=[]    
for i in range(1,7):
    result.append(MonteCarlo(10**i))

# Actual probability value = 21.7376%
# Plot number of numdom points and probability
plt.xscale('log')
plt.plot([10**i for i in range(1,7)],result)
plt.scatter([10**i for i in range(1,7)],result)