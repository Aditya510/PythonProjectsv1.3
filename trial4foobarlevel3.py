def answer(lisa):
    lisa = sorted(lisa)
    pairs = []
    for i in lisa:
        for j in lisa:
            if j > i and j % i == 0:
                pairs.append([i,j])

    countlist = []
    for item in lisa:
        count = 0
        for element in pairs:
            if element[1] == item:
                count += 1
        countlist.append(count)

    result = []
    for i in range(len(lisa)):
        count = 0
        
        for element in pairs:
            if element[1] == lisa[i]:
                
                count += countlist[lisa.index(element[0])]
                
        result.append(count)
    suma = 0
    for item in result:
        suma += item
    return suma
print(answer([1,2,3,4,5,6]))
