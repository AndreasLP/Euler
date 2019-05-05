import gcd
def lcm(a,b):
    print('Abort mission!')
    if a%1!=0: a=int(a)
    if b%1!=0: b=int(b)
    if a > b:
        a,b=b,a
    ab = a*b
    am = [i for i in range(a,ab+1,a)]
    bm = [i for i in range(b,ab+1,b)]
    for i in am:
        if i in bm: return i
    return ab
def lcm2(a,b):
    if a%1!=0: a=int(a)
    if b%1!=0: b=int(b)
    return int(a*b/gcd.gcd(a,b))
