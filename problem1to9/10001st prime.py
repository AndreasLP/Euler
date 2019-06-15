from isPrime import *

primes = []
i = 2
while len(primes)<10002:
    if isPrime(i): primes.append(i)
    i=i+1
print(primes[0:20])
print(primes[10000])
