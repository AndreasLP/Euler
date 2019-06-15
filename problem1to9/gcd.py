def gcd(a,b):

    if a>b:
        c=max(a,b)
        a=min(a,b)
        b=c
    while a!=0 and b!=0:
        c=a
        a=b%a
        b=c
        if a>b:
            c=max(a,b)
            a=min(a,b)
            b=c
    return max(a,b)
