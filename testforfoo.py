import itertools


def answer(lisa):
    count = 0
    if len(lisa) == 2:
        return 0
    lisa = sorted(lisa)
    for item in itertools.combinations(lisa,2):
        index = lisa.index(item[1])
        if item[1] % item[0] == 0:
            for subitem in lisa[index:]:
                if subitem > item[1]:
                    if subitem % item[1] == 0:
                        count += 1
    print("Hello")                    
    return count
