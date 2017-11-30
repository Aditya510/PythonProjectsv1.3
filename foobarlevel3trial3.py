def answer(lisa):
    count = 0
    if len(lisa) == 2:
        return 0
    lisa = sorted(lisa)
    for item in lisa:
        
        for subitem in lisa[lisa.index(item)+1:]:
            if subitem % item == 0:
                for subsubitem in lisa[lisa.index(subitem)+1:]:
                    if subsubitem % subitem == 0:
                        count +=1
    return count

print(answer([1,2,3,4,5,6]))
