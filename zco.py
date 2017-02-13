import time
start = time.time()
x = [ item for item in range(0,1000000) if ((item % 6 == 1) or (item % 6 == 5))]
somedefaultprimes = [5,7,11,13,17,19,23,29]
for itera in somedefaultprimes:
    x= [item for item in x if item % itera != 0]
    
print(x)
##x = [ item for item in x if item % 5 != 0]
##x = [ item for item in x if item % 7 != 0]
##x = [ item for item in x if item % 11 != 0]
##x = [ item for item in x if item % 1 != 0]
##x = [ item for item in x if item % 11 != 0]
mlist = []
totryval  = int(1.25*(1000000**0.5))

trylist = [item for item in range(1,totryval,2) if ((item % 2 != 0) and (item % 3 != 0) and (item % 7 != 0) and (item % 5 != 0) and (item % 13 != 0) and (item % 17 != 0) and (item % 19 != 0) and (item % 23 != 0) and (item % 29 != 0))]
trylist.remove(1)

for item in x:
    val = True
    
    for iter in trylist:

                   if item % iter == 0:
                   
                       val = False
    if val == True:
        mlist.append(item)
        
print(mlist[-1])
end = time.time() - start
print(end)
