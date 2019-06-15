from isPrime import isPrime
from primes_to_n import list_primes
import itertools as it
#primes = list_primes(10**10)
#print("part 1")
def is_pandigital(s):
    for d in range(1,len(s)+1):
        if s.count(str(d)) != 1:
            return False
    return True 
cand = set()
for d in range(2,9):
    for i in it.permutations([str(i) for i in range(1,d+1)]):
        p = ''.join(i)
        if isPrime(int(p)):
            if is_pandigital(p):
                cand.add(p)
print("count:",len(cand))                
print("max:",max(cand))
