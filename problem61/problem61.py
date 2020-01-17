import itertools as it
import sys

def triangle(n):
    return int((n*(n+1))/2)
def square(n):
    return int(n*n)
def pentagonal(n):
    return int((n*(3*n-1))/2)
def hexagonal(n):
    return int(n*(2*n-1))
def heptagonal(n):
    return int((n*(5*n-3))/2)
def octagonal(n):
    return int(n*(3*n-2))
n = 10
N = 150
#print(triangle(n),triangle(N))
#print(square(n),square(N))
#print(pentagonal(n),pentagonal(N))
#print(hexagonal(n),hexagonal(N))
#print(heptagonal(n),heptagonal(N))
#print(octagonal(n),octagonal(N))

def gen(n,N,func):
    out = []
    for i in range(n,N):
        s = str(func(i))
        if len(s) == 4:
            out.append(s)
        elif len(s) > 4:
            break
    return out 

def followed(i,s):
    out = []
    for j in s:
        if i[2:]==j[0:2] and j[2]!="0":
           out.append(j)
    if len(out)>=1:
        return out
    else:
        return []



tri = gen(n,N,triangle)
sq = gen(n,N,square)
pen = gen(n,N,pentagonal)
hexa = gen(n,N,hexagonal)
hep = gen(n,N,heptagonal)
octa = gen(n,N,octagonal)


#print(tri)
#print(sq)
#print(pen)
#print(hexa)
#print(hep)
#print(octa)
#for i in tri:
#    print(i)
#    print(followed(i,sq))
#    print(followed(i,pen))
#    print(followed(i,hexa))
#    print(followed(i,hep))
#    print(followed(i,octa))
#    print("\n")

sets = [sq,pen,hexa,hep,octa]

for per in it.permutations(range(5)):
    for i1 in tri:
        tmp1 = followed(i1,sets[per[0]])
        if len(tmp1)>0:
            for i2 in tmp1:
                tmp2 = followed(i2,sets[per[1]])
                if len(tmp2) > 0:
                    for i3 in tmp2:
                        tmp3 = followed(i3,sets[per[2]])
                        if len(tmp3) > 0:
                            for i4 in tmp3:
                                tmp4 = followed(i4,sets[per[3]])
                                if len(tmp4)>0:
                                    for i5 in tmp4:
                                        tmp5 = followed(i5,sets[per[4]])
                                        if len(tmp5) > 0:
                                            for i6 in tmp5:
                                                if i1[0:2]==i6[2:]:
                                                    print(i1,i2,i3,i4,i5,i6)
                                                    print(sum([int(i) for i in [i1,i2,i3,i4,i5,i6]]))
                                                    print(per)
                                                    sys.exit(0)




