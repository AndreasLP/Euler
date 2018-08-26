from Primes import *
from isPrime import *
def LargestPrimeFactor(n):
    if isPrime(n): return 1
    p = Primes(int(n**(0.5))+3)
    p.reverse()
    for i in p:
        if n%i==0: return i
