import numpy as np

def sum_proper_div(N):
    pot_div = np.arange(1,int(N/2)+1)
    return np.sum(pot_div[N%pot_div==0])


sum_val = 0

for num in range(10001):
    sum_div = sum_proper_div(num)
    if num != sum_div and num==sum_proper_div(sum_div):
        sum_val += num

print(sum_val)        

