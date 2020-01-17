import sys
import math
m = 6
def digits(n):
    d = [c for c in str(n)]
    d.sort()
    return d

def test(n):
    d = digits(n)
    for i in range(2,m+1):
        d_test = digits(n*i)
        if d != d_test:
            return False
    return True    

p = 0
while True:
    top = 10**(p+1)
    for n in range(10**p,int(top/m)):
        if n == 125874:
            print("Test 1")
        if test(n):
            print(n)
            sys.exit(0)
    p += 1        
    print(10**p)
