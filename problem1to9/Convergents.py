from math import floor
def Convergents(n,terms=10):
    print("Virker kun til 16 decimaler")
    numbers = [floor(n),[]]
    n = n-floor(n)
    idx = 1
    while n !=0 and idx<=terms:
        inv = 1/n
        f_inv = floor(inv)
        numbers[1].append(f_inv)
        n = inv - f_inv
        idx+=1
    return numbers
