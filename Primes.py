from isPrime import *
def Primes(n):
    return [i for i in range(1,int(n)+1) if isPrime(i)]
