n = 200
vallist = []
while n < 202:
    
    masterlist =  [ ["*" for i in range(n)] for i in range(n)]
    for i in range(n):
        masterlist[i][0] = 1
        masterlist[0][i] = 1
    print(masterlist)
    for item in range(1,n):
        for sub in range(1,n):
            masterlist[item][sub] = masterlist[item-1][sub]+masterlist[item][sub-1]
    x =   (masterlist[n-1][n-1])
    print(x)
    vallist.append(x)
    n += 1

print(vallist[1]/vallist[0])
