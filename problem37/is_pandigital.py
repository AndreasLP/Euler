def is_pandigital_9(s):
    if len(s)!=9:
        return False
    for d in range(1,10):
        if s.count(str(d)) != 1:
            return False
    return True

