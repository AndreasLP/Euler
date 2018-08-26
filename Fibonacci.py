def Fibonacci(s1=0,s2=1,limit=100000):
    nxt = s1+s2
    seq = [s1,s2]
    while nxt<=limit:
        seq.append(nxt)
        s1=s2
        s2=nxt
        nxt=s1+s2
    return seq
