s= ""
l=0
d=[]
for n in range(1,10**6):
    
    if l>10**6:
        break
    n = str(n)
    l+=len(n)
    s=s+n
print(int(s[0])*int(s[9])*int(s[10**2-1])*int(s[10**3-1])*int(s[10**4-1])*int(s[10**5-1])*int(s[10**6-1]))
