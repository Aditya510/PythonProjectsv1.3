k = 5
count = 0
list1 = [14,2,3,10,4]
list2 = [2,5,3,7,1]
def sortlists(l1,l2):
    l1.sort()
    l2.sort()
def checkskew(l1,l2):
    currentskew = sorted(l1)[-1] + sorted(l2)[-1]
    return currentskew

print(checkskew(list1,list2))
while count <= k:
    sortlists(list1,list2)
    maxval = max(list1[-1],list2[-1])
    if maxval in list1:
        maxvalin1 = True
    else :maxvalin1 = False
    print(maxvalin1)
    if maxvalin1:
        list1.append(list2[-1])
        list2.append(list1[0])
        sortlists(list1,list2)
        del list1[0]
        del list2[-1]
        
        print(list1,list2)
        print(checkskew(list1,list2))
    count += 1
        
    
