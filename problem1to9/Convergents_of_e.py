import SumOfDigits
def frac(convers):
    numb = convers[1]

    nu = 1
    de = numb[-1]
    numb.reverse()
    print(numb)
    for i in numb[1:]:
        print(i)
        nu += i*de
        nu,de = de,nu
    nu += convers[0]*de
    return [nu,de]

n = 99
con = []
k = 1
for i in range(1,n+1):
    if (i+1)%3==0:
        con.append(k*2)
        k += 1
    else:
        con.append(1)
convergent = [2,con]
print(convergent)
res=frac(convergent)
print(res)
print(SumOfDigits.sum(res[0]))
