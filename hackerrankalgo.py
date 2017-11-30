#!/bin/python3
import itertools
q= int(input())


for hel in range(q):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c1 = list(map(int, input().strip().split(' ')))
    c2 = list(map(int, input().strip().split(' ')))
    found = False
    try:
        for item in itertools.permutations(c1):
            for subitem in itertools.permutations(c2):
                print(item,subitem)
                bool = True
                for i in range(n):
                    print(c1[i] + c2[i], k)
                    if c1[i] + c2[i] < k:
                        bool = False
                        
                        break
                if bool == True:
                    print(1)
                    raise ValueError
    except :
        found = True

    print(found)
