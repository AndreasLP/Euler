import numpy as np
from primes_to_n import *

def prime_factors(n):
    if n<1:
        return []
    elif n==1:
        return [(1,1)]
    ps = primes_to_n(int(n/2)+1)
    factors = ps[n%ps==0]
    p_factors = []
    for f in factors:
        count = 1
        while n%(f**(count+1))==0:
            count += 1
        p_factors.append((f,count))
            
            
    if len(p_factors)==0:
        return [(n,1)]
    else:
        return p_factors 
