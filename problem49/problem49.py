from primes_to_n import primes_to_n
import itertools as it
import numpy as np
primes = np.array(primes_to_n(10**4))
pot_p = primes[primes>=10**3]
p_fams = []
#print(1487 in pot_p)
for p in pot_p:
    #print(len(pot_p),p) 
    p_fam = set()
    
    for cand in it.permutations([c for c in str(p)]):
        num = int(''.join(cand))
        if num in pot_p:
            p_fam.add(num)

    out = True

    p_fam = list(p_fam) 
    p_fam.sort()
    
    if p_fam in p_fams:
        continue

    for i in range(len(p_fam)-2):
        for j in range(i+1,len(p_fam)-1):
            diff = p_fam[j]-p_fam[i]
            for k in range(j+1,len(p_fam)):
                if diff==(p_fam[k]-p_fam[j]):
                    p_fams.append(p_fam)
                    print(p_fam)
                    print(i,j,k)
                    print(p_fam[i],p_fam[j],p_fam[k])
                    print(str(p_fam[i])+str(p_fam[j])+str(p_fam[k]))



