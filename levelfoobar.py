import itertools
import random

def answer(lisa):
    count = 0
    if len(lisa) == 2:
        return 0
    lisa = sorted(lisa)
    for item in itertools.combinations(lisa,2):
        
        if item[1] % item[0] == 0:
            
            for subitem in lisa:
                if subitem > item[1]:
                    
                    if subitem % item[1] == 0:
                        count += 1
                        
    return count

lisa= []
for item in range(1,2000):
    lisa.append(random.randint(1,1000000))
print(lisa)
print(answer(lisa))

