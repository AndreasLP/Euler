import sys
from math import sqrt,log,pi
def coin_sum(amount):
    ways = [0]*(amount+1)
    ways[0] = 1;
    for i in range(1,amount+1):
        for j in range(i,amount+1):
            ways[j] = ways[j] + ways[j - i]

    return ways[amount];


m = 10**6
C = pi * sqrt(2/3)
for n in range(5,700,1):
    #print(n,coin_sum(n))
    print(C*sqrt(n)-log(coin_sum(n)))
    #print(' ')
    if(coin_sum(n)%m == 0): 
        sys.exit() 

#for amount in range(10,101,500): 
#    print(coin_sum(amount));


