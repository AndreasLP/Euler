from primes_to_n import *
from isPrime import *
primes = primes_to_n(10**7)

def is_truncatable(p):
    if not isPrime(p):
        return False
    for d in range(1,len(str(p))):
        #print(str(p)[0:-d])
        #print(str(p)[d:])
        #if int(str(p)[0:-d]) not in primes or int(str(p)[d:]) not in primes:
        if not isPrime(int(str(p)[0:-d])) or not isPrime(int(str(p)[d:])):    
            return False
    return True    

t = set()

for p in primes[4:]:
    if is_truncatable(p):
        t.add(p)
        if len(t)>=11:
            break
# Know len(t)==10
s = set()
m = max(t)
for cand in [2, 3, 5, 7]:
    for p in t:
        if is_truncatable(int(str(p)+str(cand))) and m<int(str(p)+str(cand)):
            s.add(int(str(p)+str(cand)))
            print(int(str(p)+str(cand)))
        elif is_truncatable(int(str(cand)+str(p))) and m<int(str(cand)+str(p)):
            s.add(int(str(cand)+str(p)))
            print(int(str(cand)+str(p)))
t = s|t

print(t)
print(len(t))
print(sum(t))

