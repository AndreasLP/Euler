from math import sqrt
from fractions import Fraction
def chakravala(D):
    b = 1
    a = int(round(sqrt(D)))
    D_sqrt = sqrt(D)
    k = int(a*a-D)
    while (k != 1):
        k_abs=abs(k)
        M = lambda T: abs(k) * T + x
        for i in range(0,int(abs(k))):
            if (a + i*b)%k == 0:
                x = i
                break
        t = int((sqrt(D)-x)/abs(k))
        if abs(D - M(t)**2) > abs(D - M(t+1)**2): t += 1
        m = M(t)
        #print("m: ",m)#," t0: ",t0," s: ", s)
        a, b = int(Fraction(a*m+D*b,abs(k))), int(Fraction(a+b*m,abs(k)))
        k = Fraction(m**2-D,k)
        #print("a: ",a,"b: ",b, "k: " ,k)
        if k==-1:
            return int(2*a**2-1),int(2*a*b)
        if abs(k)==2:
            return int(a**2+int(k/2)),int(a*b)
        if k==4:
            if a%2==0:
                return 2*(int(Fraction(a,2))**2)-1, int(a*b)
            else:
                u = int(Fraction(a-1,2))
                return a*(2*u**2 + a-2), 2*u*(u + 1)*b
        if k==-4:
            if a%2==0:
                return 2*(int(Fraction(a,2))**2)+1, (b)
            else:
                p = Fraction((a**2+2)*((a**2+1)*(a**2+3)-2),2)
                q = Fraction(a*b*(a**2+1)*(a**2+3),2)
                return p,q


    return a,b
max_x = 0
max_x_D=0
max_D = 1000

for i in range(max_D):
    sqrt_i = int(sqrt(i));
    if sqrt_i*sqrt_i!=i:
        s = chakravala(i)
        if s[0]> max_x: max_x,max_x_D = s[0], i

print(max_x_D)
