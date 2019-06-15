def gcd(a,b):

    if a>b:
        c=a
        a=b
        b=c
    while a!=0:
        c=a
        a=b%a
        b=c
    return a
