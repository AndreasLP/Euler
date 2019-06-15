import numpy as np

def is_pandigit_prod(l,r):
    
    p = l*r
    l_s = str(l)
    r_s = str(r)
    p_s = str(p)
    if len(l_s)+len(r_s)+len(p_s) != 9:
        return False
    for i in [str(j) for j in range(1,10)]:
        if l_s.count(i)+r_s.count(i)+p_s.count(i) != 1:
            return False
    
    return True

prod = set()
for l in range(1,100):
    if l > 9:
        begin = 123
    else:
        begin = 1234
    
    for r in range(begin,int(10000/l)+1):
        if is_pandigit_prod(l,r):
            print("l:",l,"r:",r)
            prod.add(l*r)
print("Combinations:",len(prod))
print("Sum:",sum(prod))
