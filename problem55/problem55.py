from is_palindrome import is_palindrome

def is_lychrel(n):
    count = 0
    new = n
    while count <= 50:
        new = new + int(str(new)[::-1])
        if is_palindrome(str(new)):
            return False
        count += 1
    return True    


tot = 0
for i in range(1,10000):
    if is_lychrel(i):
        tot += 1
        #print(i)
print(tot)        
