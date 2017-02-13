def hamming(n):
    lista = []
    a = 0
    for x in range(0,22):
      for y in range(0,16):
        for z in range(0,16):
            app = (2**(x) *(3**(y))*(5**z))
            a += 1
            lista.append(app)
    lista.sort()
    print(lista[134:137], a)
    return(lista[n-1])
    print(lista[134:137])
print(hamming(110))
def new():
    lista = [2**x + 3**y + 4**z for x in range(22) for y in range(22) for z in range(22)]
    

new()
