from math import sqrt
from collections import Counter as C
N = 10000
def first_div(n):
    if n%2==0:
        return 2
    else:
        for d in range(3,int(sqrt(n))+1):
            if n%d==0:
                return d
    return n

def prime_factors_fac(n):
    out = [None]*(n-1)
    for idx,i in enumerate(range(2,n+1)):
        d = first_div(i)
        if d==i:
            out[idx] = [d]
        else:
            out[idx] = [d]+out[int(i/d)-2]
    return out
tmp = prime_factors_fac(N)
factors = tmp[0]
for t in tmp[1:]:
    factors = factors + t
factors.sort()    
count = C(factors)
print(count)
