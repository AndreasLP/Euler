import numpy as np
from collections import Counter
def sorted_cube(N):
    return (''.join([str(j) for j in np.sort([int(i) for i in str(N**3)])]))


N = 5
found = False
for power in range(16):
    lower = int(np.ceil(10**(power/3)))
    upper = int(np.floor((10**(power+1)-1)**(1/3)))
    #print(10**power,lower**3,upper**3,10**(power+1))
    nums = np.arange(lower,upper+1)
    res = [None]*len(nums)
    for idx,num in enumerate(nums):
        res[idx]=sorted_cube(num)
    c = Counter(res)
    for i in c.most_common(len(c)):
        if i[1]==N:
            found = True
            print(i)
            print(nums[res.index(i[0])])
            print(nums[res.index(i[0])]**3)
            break
    if found:        
        break
