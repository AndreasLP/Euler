import numpy as np

fac = [np.math.factorial(i) for i in range(10)]

def factorial_digit_sum(n):
    sum_val = 0
    for c in str(n):
        sum_val += fac[int(c)]
    return sum_val

sum_num = 0
for n in range(3,10**7+1):
    if n==factorial_digit_sum(n):
        sum_num+=n
        print(n)

print("Sum:",sum_num)        
