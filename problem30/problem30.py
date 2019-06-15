#from math import *
sum_val = 0
def sum_fifth(n):
    sum_pow = 0
    for c in str(n):
        sum_pow += int(c)**5
    return sum_pow

for i in range(10,1000000):
    if i == sum_fifth(i):
        print(i)
        sum_val += i

print('Sum: ', sum_val)
