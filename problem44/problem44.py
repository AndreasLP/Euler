import numpy as np

def test(p_1,p_2,p=False):
    s = p_1 + p_2
    #s_p =((1+np.sqrt(1+24*s))/6)
    d = abs(p_1-p_2)
    #d_p =((1+np.sqrt(1+24*d))/6)      
    #if d_p==int(d_p) and s_p==int(s_p):
    if ((1+np.sqrt(1+24*s))/6)%1==0 and ((1+np.sqrt(1+24*d))/6)%1==0:
        return True
    else:
        return False
    

k_m = 0
j_m = 0

k=1
p_k = 1
p_k1 = 5
notFound = True
while notFound: 
    for j in range(k,0,-1):
        p_j = (j*(3*j-1))/2
        if k==2167 and j==1020:
            test(p_k,p_j,True)
        if test(p_k,p_j):
            m = p_k-p_j
            k_m = k
            j_m = j
            notFound = False
            break
    k += 1
    p_k = p_k1
    p_k1 = ((k+1)*(3*(k+1)-1))/2        
print(k_m,j_m,m)
