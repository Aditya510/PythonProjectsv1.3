def answer(lista):
    count = 0
    for i in range(1,len(lista)-1):
        left = len([item for item in lista[:i] if lista[i] % item == 0])
        right = len([item for item in lista[i+1:] if item % lista[i] == 0])
        count += (left*right)
    return count


