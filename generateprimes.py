def gap(g, m, n):
    lista = [elem for elem in range(m,n+1) if checkforprime(elem)]
    for x in range(0, len(lista)-1):
        if lista[x+1] - lista[x] == g:
            return([lista[x],lista[x+1]])
    else:
        return None


def checkforprime(x):
    for y in range(2,x):
        if x%y == 0:
            return False
    return True

def gaap(g, m, n):
    lista = [elem for elem in range(m,n+1) if checkforprime(elem)]
    return [(lista[x],lista[x+1]) for x in range(0, len(lista)-1) if lista[x+1] - lista[x] == g ][0]

def primegenerator(y):
    fullist = [x for x in range(y//2,y+1) if x%2 != 0]
    list1 = [x for x in fullist if x%3 != 0]
    list2 = [x for x in list1 if x%5 != 0]
    list3 = [x for x in list2 if x%7 != 0]
    lista = [elem for elem in list3 if checkforprime(elem)]
    print(lista[-1])

def apg(y):
    lista = [elem for elem in range(2,y+1) if checkforprime(elem)]
    print(lista[-1])
print(gap(2,100,110))
print(gaap(2,100,110))

primegenerator(98000)

