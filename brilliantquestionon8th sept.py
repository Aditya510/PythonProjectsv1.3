import itertools
import sys
sys.setrecursionlimit(10000)
lis = [x for x in range(1,20)]
vals = []
def sumlis(lis):
    if len(lis) == 1:
        return lis[0]
    else:
        newlis = []
        for i in range(0,len(lis)-1):
            newlis.append(lis[i] + lis[i+1])
        return sumlis(newlis)

for item in itertools.permutations(lis):
    vals.append(sumlis(item))

print(max(vals) - min(vals))
    
