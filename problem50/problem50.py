import sys
from primes_to_n import *
M = 10**6
primes = primes_to_n(M)

t = 0
N = 0
for p in primes:
    t += p
    if t<M:
        N += 1
    else:
        break
L = len(primes)    
for num in range(N,0,-1):
    sums = [sum(primes[(0+i):(num+i)]) for i in range(0,L-num)]
    for pot in sums[::-1]:
        if pot in primes:
            print(num,pot)
            sys.exit(0)


