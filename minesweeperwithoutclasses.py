import random

def getcors():
    cors = []
    while len(cors)<15:
        y = random.randint(0,8)
        x = random.randint(0,8)
        if (x,y) not in cors:
            cors.append((x,y))
    return cors

def checkmine(x,y,cors):
        if (x,y) in cors:
            return True
        return False


def getcount(x,y,cors):
        if (x,y) in cors:
            return "M"
        count = 0
        if  checkmine(x - 1,y,cors): count +=1
        if  checkmine(x - 1,y+1,cors): count +=1
        if  checkmine(x - 1,y-1,cors): count +=1
        if  checkmine(x ,y+1,cors): count +=1
        if  checkmine(x ,y-1,cors): count +=1
        if  checkmine(x + 1,y+1,cors): count +=1
        if  checkmine(x + 1,y,cors): count +=1
        if  checkmine(x + 1,y-1,cors): count +=1
        return count
    



cors = getcors()

overboard = [ ["X"]*9 for i in range(9) ]

baat = []
for i in range(0,9):
    toappend= []
    for j in range(0,9):
        
        k=getcount(i,j,cors)
        
        toappend.append(k)
    baat.append(toappend)

def checkforitem(overboard,item):
    for line in overboard:
        if item in line:
            return False
    return True


def makelist(k):
    returnlist = [ ['x']*9 for i in range(9) ]
    for i in range(0,9):
        for j in range(0,9):
            returnlist[i][j] = []
             
            if k[i][j] != 0:
                continue
            try:
                if k[i-1][j] == 0:
                    returnlist[i][j].append((i-1,j))
            except:pass
            try :
                if k[i-1][j-1] == 0:
                    returnlist[i][j].append((i-1,j-1))
            except:pass
            try:
                if k[i-1][j+1] == 0:
                    returnlist[i][j].append((i-1,j+1))
            except:pass
            try:
                if k[i][j+1] == 0:
                    returnlist[i][j].append((i,j+1))
            except:pass
            try:
                if k[i+1][j] == 0:
                    returnlist[i][j].append((i+1,j))
            except:pass
            try:
                if k[i][j-1] == 0:
                    returnlist[i][j].append((i,j-1))
            except:pass
            try:
                if k[i+1][j-1] == 0:
                    returnlist[i][j].append((i+1,j-1))
            except:pass
            try:
                if k[i+1][j+1] == 0:
                    returnlist[i][j].append((i+1,j+1))
            except:pass
    for a in returnlist:
        for b in a:
            for c in b:
                
                if c[0] < 0 or c[1]  < 0:
                    
                    b.remove(c)
    for a in returnlist:
        for b in a:
            for c in b:
                
                if c[0] < 0 or c[1]  < 0:
                    
                    b.remove(c)
                

    return returnlist

def explodeall(baat,overboard,x,y):
    
    
    
    overboard[x][y] = baat[x][y]
    
    if len(makelist(baat)[x][y]) > 0:
        for item in makelist(baat)[x][y]:
            if overboard[item[0]][item[1]] == "X":
                explodeall(baat,overboard,item[0],item[1])
            
        

for item in baat:
    print(item)

for item in makelist(baat):
    print(item)

t = tuple(input("vals"))
if baat[int(t[0])][int(t[2])] == "M":
    print("You lose")

explodeall(baat,overboard,int(t[0]),int(t[2]))

for item in overboard:
    print(item)
    

