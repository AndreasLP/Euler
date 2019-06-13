from math import log2
def dec2bin(n):
    v = [0]*(int(log2(n))+1)
    for idx,i in enumerate(range(int(log2(n)),-1,-1)):
        if n==0:
            return v
        if 2**i <= n:
            n-=2**i
            v[idx]=1
    return v        

