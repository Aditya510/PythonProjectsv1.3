def answer(M, F):
    count = 0
    m = int(M)
    f = int(F)
    while m != f :
        if m - f > 0:
            count = (m/f)
            print(m,f)
            print(count)
            m = m%f
            
        elif f - m > 0:
            count = (f/m)
            print(f,m)
            print(count)
            f = f%m
    if m == 1:
        return str(count)
    else :
        return "impossible"

print(answer(4,7))
