from is_palindrome import is_palindrome
from base2base import dec2bin

sum_out = 0

for i in range(1,10**6):
    if is_palindrome(str(i)):
        if is_palindrome(dec2bin(i)):
            sum_out += i

print(sum_out)            
