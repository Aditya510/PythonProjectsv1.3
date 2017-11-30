import itertools

def large(lista):
    lista = sorted(lista)
    string = ""
    for item in lista:
        string+= str(item)
    return(int(string[::-1]))

def sumt(lista):
    lista = sorted(lista)
    suma = 0
    for item in lista:
        suma+= item
    return(suma)

def answer(lisa):
    if sumt(lisa) % 3 == 0:
        return(large(lisa))
    else:
        gotanswer = False
        for i in range(len(lisa),1,-1):
            maxi = 0
            for item in itertools.combinations(lisa,i-1):
                if sumt(item) % 3 == 0:
                    gotanswer = True
                    val = large(item)
                    if val > maxi :
                        maxi = val
            if gotanswer:
                break
        return(maxi)
