import numpy as np


def solutions(p):
    count = 0
    t = int(np.ceil(p/2))
    for a in range(1,t):
        for b in range(1,a):
            c = p - a - b
            if c**2==(a**2+b**2):
                count+=1
    return count            


max_count = 0
max_p = 0

for p in range(2,1000+1,2):
    if p%100==0: 
        print(p)
    cnt = solutions(p)
    if cnt>max_count:
        max_count = cnt
        max_p = p

print("Count:",max_count)
print("p:",max_p)

