from listOfPrimes import rwh_primes1
import numpy as np
from itertools import combinations_with_replacement

primes = rwh_primes1(100000)
all_primes = rwh_primes1(100000)
N = 2

for prime in primes:
    if str(prime).count("0") < N and str(prime).count("1") < N and str(prime).count("2") < N:
        primes.remove(prime)

numbers = np.arange(0, 10)
families = [None] * len(primes) # Important change


for idx, prime in enumerate(primes):
    s = str(prime)
    n = len(s)
    for k in range(N, n):
        combos = list(combinations_with_replacement(range(0, n), k))
        families[idx] = [None] * len(combos)
        for idx3, comb in enumerate(combos):
            for num in numbers:
                new = s
                for idx2 in comb:
                    new = new[:idx2] + str(num) + new[(idx2 + 1):]

                if int(new) in all_primes and len(new) == n and int(new) > prime:
                    if families[idx][idx3] is None:
                        families[idx][idx3] = [prime, int(new)]
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
    else:
        families[idx] = [0, 0]
print('step 2')

for idx, sets in enumerate(families):
    if 0 not in sets:
        for family in sets:
            if len(family) >= 6:
                print(primes[idx])
                print(family, end='\n\n')

print('step 3')

for idx, sets in enumerate(families):
    for family in sets:
        if family != 0:
            if 56003 in family:
                print(family)
