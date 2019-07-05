import itertools as it

div = [2,3,5,7,11,13,17]

def test(s):
    for i,d in enumerate(div):
        if int(s[(1+i):(4+i)])%d!=0:
            return False
    return True

sum_out = 0

o = [str(i) for i in range(10)]

for d in range(1,10):
    o.remove(str(d))
    for comb in it.permutations(o):
        s = str(d)+''.join(comb)
        if test(s):
            sum_out += int(s)

    o.append(str(d))
    o.sort()
print(sum_out)
