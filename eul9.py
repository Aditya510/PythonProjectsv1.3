def collength(i):
    suma = 0
    while i != 1:
        if i % 2 == 0:
            i = i/2
            suma += 1
        else:
            i = 3*i + 1
            suma+=1
    return(suma+1)

a = 0
for i in range(0,100):
    if collength(i) > a:
        a = collength(i)
print(a)
