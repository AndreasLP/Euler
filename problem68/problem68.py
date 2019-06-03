import itertools as it
import numpy as np
from time import time

def test_opt(opt,size):
    if size!= 5:
        sets = np.zeros((size,3))
        sets[0]=opt[0:3]
        sum_val = int(np.sum(sets[0]))
        pos=3
        for idx in range(1,size-1):
            sets[idx,0]=opt[pos]
            pos+=1
            sets[idx,1]=sets[idx-1,2]
            sets[idx,2]=opt[pos]
            pos+=1
            if int(np.sum(sets[idx])) != sum_val:
                return False,sets
        sets[size-1,0]=opt[pos]
        sets[size-1,1]=sets[size-2,2]
        sets[size-1,2]=sets[0,1]
        if int(np.sum(sets[size-1])) != sum_val:
            return False,sets
        
        sets = np.roll(sets,-np.nonzero(sets[:,0]==min(sets[:,0]))[0][0],axis=0)

        return True,sets    
    else:
        sets = np.zeros((size,3))
        sets[0,1:]=opt[0:2]
        sets[0,0]=10
        sum_val = int(np.sum(sets[0]))
        pos=2
        for idx in range(1,size-1):
            sets[idx,0]=opt[pos]
            pos+=1
            sets[idx,1]=sets[idx-1,2]
            sets[idx,2]=opt[pos]
            pos+=1
            if int(np.sum(sets[idx])) != sum_val:
                return False,sets
        sets[size-1,0]=opt[pos]
        sets[size-1,1]=sets[size-2,2]
        sets[size-1,2]=sets[0,1]
        if int(np.sum(sets[size-1])) != sum_val:
            return False,sets
        
        sets = np.roll(sets,-np.nonzero(sets[:,0]==min(sets[:,0]))[0][0],axis=0)

        return True,sets    


def gen_pos(size):
    if size != 5:
        return it.permutations(np.arange(1,size*2+1))
    else:
        return it.permutations(np.arange(1,size*2))


size=5
opts=gen_pos(size)
fits=np.zeros((1,size*3))
start = time()
for idx,opt in enumerate(opts):
    fit,sets = test_opt(opt,size)
    if fit:
        fits=np.vstack((fits,sets.flatten()))
        
part1 = time()
fits=np.unique(fits,axis=0)
fits=fits[~np.all(fits==0,axis=1)]
#print(fits)
one10 = [a for a in np.ndarray.tolist(fits) if a.count(10) <= 1]
one10=[int(c) for c in [''.join([str(int(a)) for a in b]) for b in one10]]
part2 = time()
print(one10)
print(max(one10))
print("")
print("Part 1: ",part1 - start)
print("Part 2: ",part2 - part1)
