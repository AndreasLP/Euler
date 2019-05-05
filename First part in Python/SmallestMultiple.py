import lcm
def sm(n):
    a = 1
    for i in range(2,n+1):
        a = lcm.lcm2(a,i)
    return a
