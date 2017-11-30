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

class locat(object):
    def __init__(self,cors,x,y):
        self.ope = False
        self.x  = x
        self.y = y
        if (self.x,self.y) in cors:
            self.mine = True
        else : self.mine = False
        self.cors = cors

    

    def getcount(self):
        if self.mine == True:
            return "M"
        count = 0
        if  checkmine(self.x - 1,self.y,self.cors): count +=1
        if  checkmine(self.x - 1,self.y+1,self.cors): count +=1
        if  checkmine(self.x - 1,self.y-1,self.cors): count +=1
        if  checkmine(self.x ,self.y+1,self.cors): count +=1
        if  checkmine(self.x ,self.y-1,self.cors): count +=1
        if  checkmine(self.x + 1,self.y+1,self.cors): count +=1
        if  checkmine(self.x + 1,self.y,self.cors): count +=1
        if  checkmine(self.x + 1,self.y-1,self.cors): count +=1
        return count

cors = getcors()
temp  = ["X","X","X","X","X","X","X","X","X"]


locats = list([temp]*9)



for i in range(0,9):
    for j in range(0,9):
        
        locats[i][j]=(locat(cors,i,j))


overboard = [ ["X"]*9 for i in range(9) ]

baat = []
for i in range(0,9):
    toappend= []
    for j in range(0,9):
        
        k=(locat(cors,i,j).getcount())
        
        toappend.append(k)
    baat.append(toappend)

def checkforitem(overboard,item):
    for line in overboard:
        if item in line:
            return False
    return True

print(baat)
print(overboard)


##while checkforitem(overboard,"M"):
##    toenter=  tuple(input("Enter tuple value"))
##    print(toenter)
##    x = int(toenter[0])
##    y = int(toenter[2])
##    
##    overboard[x][y] = baat[x][y]
##    for item in overboard:
##        print(item)





