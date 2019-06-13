import numpy as np
#import itertools as it
#from math import sqrt

def sum_proper_div(N):
    pot_div = np.arange(1,int(N/2)+1)
    return np.sum(pot_div[N%pot_div==0])


test = set(range(1,28123))
abundant = []
a_sum = set()

for i in range(12,28123):
    if i<sum_proper_div(i):
        abundant.append(i)

for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
        a_sum.add(abundant[i]+abundant[j])

print(sum(test-a_sum))


