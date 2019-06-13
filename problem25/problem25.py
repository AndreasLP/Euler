import numpy as np
from math import log10 
f1 = 1
f2 = 1
n = 2
while(log10(f2)<999):
    n,f1,f2 = n+1,f2,f1+f2
print(n)    
