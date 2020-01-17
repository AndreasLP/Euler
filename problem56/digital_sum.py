
def digital_sum(n):
    s = str(n)
    out = 0
    for c in s:
        out += int(c)
    return out    
