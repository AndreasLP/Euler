from isPrime import *
def Primes(n):
    return [i for i in range(1,int(n)) if isPrime(i)]
