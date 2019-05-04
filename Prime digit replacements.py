from listOfPrimes import rwh_primes1
import numpy as np
from itertools import combinations

primes = rwh_primes1(100000)
numbers = np.arange(0, 10)
families = [None] * len(primes) # Important change

for idx, prime in enumerate(primes):
    s = str(prime)
    n = len(s)
    for k in range(1, n+1):
        combos = list(combinations(range(0, n), k))
        families[idx] = [None] * len(combos)
        for idx3, comb in enumerate(combos):
            for num in numbers:
                new = s
                for idx2 in comb:
                    new = new[:idx2] + str(num) + new[(idx2 + 1):]
                if int(new) in primes and len(new) == n and int(new) > prime:
                    if families[idx][idx3] is None:
                        families[idx][idx3] = [int(new)]
                    elif int(new) not in families[idx][idx3]:
                        families[idx][idx3].append(int(new))

print('step 1')

for idx in range(0, len(families)):
    if families[idx] is not None:
        for idx2 in range(0, len(families[idx])):
            if families[idx][idx2] is not None:
                base = int(np.log10(primes[idx]))
                families[idx][idx2] = [i for i in families[idx][idx2] if int(np.log10(i)) == base]
            else:
                families[idx][idx2] = [0]
print('step 2')

for idx, sets in enumerate(families):
    for family in sets:
        if len(family) >= 7:
            print(primes[idx])
            print(family, end='\n\n')

print('step 3')

for idx, sets in enumerate(families):
    for family in sets:
        if 56003 in family:
            print(family)