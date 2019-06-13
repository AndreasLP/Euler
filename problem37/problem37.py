from is_pandigital import is_pandigital_9

pos = set()

for test in range(2,10**5+1):
    s = ""
    n = 1
    while(len(s)<9):
        s += str(test*n)
        n += 1
    if is_pandigital_9(s):    
        pos.add(s)
print(max(pos))
print(pos)
