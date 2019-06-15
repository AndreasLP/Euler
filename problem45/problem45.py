N = 10**6

#tri = {int((n*(n+1))/2) for n in range(1,N)}
pen = {int((n*(3*n-1))/2) for n in range(1,N)}
hex = {n*(2*n-1) for n in range(1,N)}

print(pen & hex)
