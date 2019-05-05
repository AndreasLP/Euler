from listOfPrimes import rwh_primes1
import numpy as np
from itertools import combinations_with_replacement


def eight_family(prime, primes, r):
    s_prime = str(prime)
    count = 0
    base = int(np.log10(int(prime)))
    for num in '0123456789':
        if int(s_prime.replace(r, num)) in primes and int(np.log10(int(s_prime.replace(r, num)))) == base:
            count += 1

    return count == 8


primes = rwh_primes1(1000000)
for prime in primes:
    s = str(prime)
    if prime > 100000 and ((s.count("0") == 3 and eight_family(prime, primes, "0"))
                           or (s.count("1") == 3 and eight_family(prime, primes, "1"))
                           or (s.count("2") == 3 and eight_family(prime, primes, "2"))):
        print(prime)


# all_primes = rwh_primes1(100000)
# N = 2
#
# for prime in primes:
#     if str(prime).count("0") < N and str(prime).count("1") < N and str(prime).count("2") < N:
#         primes.remove(prime)
#
# numbers = np.arange(0, 10)
# families = [None] * len(primes) # Important change
#
#
# for idx, prime in enumerate(primes):
#     s = str(prime)
#     n = len(s)
#     for k in range(N, n):
#         combos = list(combinations_with_replacement(range(0, n), k))
#         families[idx] = [None] * len(combos)
#         for idx3, comb in enumerate(combos):
#             for num in numbers:
#                 new = s
#                 for idx2 in comb:
#                     new = new[:idx2] + str(num) + new[(idx2 + 1):]
#
#                 if int(new) in all_primes and len(new) == n and int(new) > prime:
#                     if families[idx][idx3] is None:
#                         families[idx][idx3] = [prime, int(new)]
#                     elif int(new) not in families[idx][idx3]:
#                         families[idx][idx3].append(int(new))
#
# print('step 1')
#
# for idx in range(0, len(families)):
#     if families[idx] is not None:
#         for idx2 in range(0, len(families[idx])):
#             if families[idx][idx2] is not None:
#                 base = int(np.log10(primes[idx]))
#                 families[idx][idx2] = [i for i in families[idx][idx2] if int(np.log10(i)) == base]
#             else:
#                 families[idx][idx2] = [0]
#     else:
#         families[idx] = [0, 0]
# print('step 2')
#
# for idx, sets in enumerate(families):
#     if 0 not in sets:
#         for family in sets:
#             if len(family) >= 6:
#                 print(primes[idx])
#                 print(family, end='\n\n')
#
# print('step 3')
#
# for idx, sets in enumerate(families):
#     for family in sets:
#         if family != 0:
#             if 56003 in family:
#                 print(family)
