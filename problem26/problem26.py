from primes_to_n import *

N = 1000

for d in primes_to_n(N)[::-1]:
    period = 1
    while pow(10, period) % d != 1: period += 1
    if d-1 == period:
        print("Done",d)
        break

    #while(pow(10,period)%d!=1):
    #    period += 1
    #if d-1 == period:
    #    print(d)
    #    break
