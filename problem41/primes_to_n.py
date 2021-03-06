import numpy as np
def list_primes(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

#def primes_to_n(n):
#    sieve = np.ones(int((n/3 + (n % 6 == 2))), dtype=np.bool)
#    sieve[0] = False
#    for i in range(int(np.ceil(n**0.5)/3)+1):
#        if sieve[i]:
#            k = 3*i+1 | 1
#            sieve[int((k*k)/3)::2*k] = False
#            sieve[int(np.ceil((k*k+4*k-2*k*(i&1))/3))::2*k] = False
#    return np.r_[2, 3, ((3*np.nonzero(sieve)[0]+1) | 1)]
