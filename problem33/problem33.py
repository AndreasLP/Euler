import fractions as fr
def sim(den):
    for idx,d in enumerate(str(den)):
        for n in range(10,den,10):
            f1 = fr.Fraction(n+int(d),den)
            f2 = fr.Fraction(int(n/10),den-int(d)*10**idx)
            if f1==f2 and f1 < 1: 
                return (n+int(d),den)

        for n in range(1,10):
            f1 = fr.Fraction(n+10*int(d),den)
            f2 = fr.Fraction(n,den-int(d)*10**idx)
            if f1==f2 and f1 < 1: 
                return (n+10*int(d),den)
    return (0,0) 


def sim_2(den):
    for num in range(11,den):
        ###print(num)
        if num > 49:
            return (0,0)
        for d in range(1,10):
            ##print(d)
            if str(num).count(str(d))==1 and str(den).count(str(d))==1:
                #print(d)
                f1 = fr.Fraction(num,den)
                f2 = fr.Fraction(int(str(num).replace(str(d),'')),int(str(den).replace(str(d),'')))
                if f1==f2:
                    return (num,den)
    return (0,0)            

frac = set()
for den in range(11,100):
    if den%10!=0:
        ret = sim_2(den)
        if ret!=(0,0):
            frac.add(ret)
            print(ret)
num = 1
den = 1
for n,d in frac:
    num *= n
    den *= d
print(num,"/",den)
print(fr.Fraction(num,den))

