lis  = [1,2,3,4,5,6,7]
limit = 10
suma = 0
import time
start = time.time()
for item in lis:
    newlis = lis[:]
    newlis.remove(item)
    for aitem in newlis:
        if item + aitem < limit:
            suma += 1
            
print(suma)
end = time.time()
print(end-start)
