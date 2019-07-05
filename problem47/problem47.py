from prime_factors import *
import itertools as it


n_ele = 4
def test(f):
    #print("Test 1")
    for pf in f:
        if len(pf)!=n_ele:
            return False
    #print("Test 2")
    for comb in it.combinations(f,2):
        for i in range(n_ele):
            if comb[0][i]==comb[1][i]:
                return False
    return True



ele = list(range(1,n_ele+1))
#ele = [13,14]
f = [prime_factors(i) for i in ele]

while not test(f):
    #if ele[0]==15:
    #    break
    #print(ele)
    #print(f)
    #tmp= 0
    #for i in range(10**6):
    #    tmp*=i
    ele = [i+1 for i in ele]
    f = f[1:]+[prime_factors(ele[-1])]
    if len(f[-1])!=n_ele:
        ele = [ele[i]+n_ele for i in range(n_ele)]
        f = [prime_factors(i) for i in ele]
print(ele)
print(f)
