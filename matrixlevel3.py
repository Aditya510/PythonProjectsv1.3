import numpy as np
from numpy.linalg import inv
import fractions
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
for i in range(len(m)):
    suma = 0
    for subitem in m[i]:
        suma += subitem
    if suma != 0:
        m[i] = [x/suma for x in m[i]]



tscount = 0
for item in m:
    
    allzero = True
    for subitem in item:
        
        if subitem != 0:
            allzero = False
    if allzero == True:
        tscount += 1


q = []
r = []
for item in range(len(m)-tscount):
    row = []
    
    for i in range(len(m)-tscount):
        row.append(m[item][i])
    q.append(row)

for i in range(len(m)-tscount):
    
    row = []
    
    for item in range(len(m) - tscount ,len(m)):
        
        row.append(m[i][item])
        
    r.append(row)


q = np.array(q)
r = np.array(r)
identity = np.identity(len(q))
subtracted = np.subtract(identity,q)
subinv = inv(subtracted)
multi = np.dot(subinv,r)
multi = multi[0]
from fractions import Fraction


numerator = []
denominator = []
for item in multi:
    
    numerator.append((Fraction(str(item)).limit_denominator(1000)).numerator)
    denominator.append((Fraction(str(item)).limit_denominator(1000)).denominator)



from functools import reduce    

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def getlcm(lista):
    return reduce(lambda x, y: lcm(x, y), lista)

lcm = getlcm(denominator)

for i in range(len(denominator)):
    if denominator[i] != lcm:
        numerator[i] = int(numerator[i] * (lcm/denominator[i]))
        
        denominator[i] = lcm

answer = []
for item in numerator:
    answer.append(item)
answer.append(lcm)
print(answer)

