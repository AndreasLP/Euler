from multipleOfList import *
import numpy as np


def n_number_of_primes(n):
    if n <= 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 3]
    elif n == 3:
        return [2, 3, 5]
    elif n == 4:
        return [2, 3, 5, 7]
    list_of_primes = [2, 3, 5, 7]
    list_length = 4
    next_number = 11
    while list_length < n:
        if not isMultipleOfList(next_number, list_of_primes):
            list_of_primes.append(next_number)
            list_length += 1
            # print('Added', next_number)
        next_number += 2
        # print('Next:',next_number)
    return list_of_primes


def number_of_primes_to_n(n):
    if n <= 0:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [2, 3]
    elif n == 5:
        return [2, 3, 5]
    elif n <= 10:
        return [2, 3, 5, 7]
    list_of_primes = [2, 3, 5, 7]
    last_prime = 7
    next_number = 11
    while last_prime < n:
        if not isMultipleOfList(next_number, list_of_primes):
            if next_number > n:
                break
            list_of_primes.append(next_number)
            last_prime = next_number
            # print('Added', next_number)
        next_number += 2
        # print('Next:',next_number)
    return list_of_primes


def primes_from_2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(int((n/3 + (n % 6 == 2))), dtype=np.bool)
    sieve[0] = False
    for i in range(int(np.ceil(n**0.5)/3)+1):
        if sieve[i]:
            k = 3*i+1 | 1
            sieve[int((k*k)/3)::2*k] = False
            sieve[int(np.ceil((k*k+4*k-2*k*(i&1))/3))::2*k] = False
    return np.r_[2, 3, ((3*np.nonzero(sieve)[0]+1) | 1)]


def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * int(n/2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[int((i-1)/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1, int(n/2)) if sieve[i]]
