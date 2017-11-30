import msvcrt as m
newlist = []
def grid():
    string = ("." * 8)
    liststring= list(string)
    for x in range(0,9):
        print(string)
        newlist.append(liststring)

        

def rowcheck(lineno):
    checkline = newlist[lineno-1]
    print(checkline.count("X"))
    if checkline.count("X")>1:
        print("Wrong!")
collist = []
def coloumncheck(colno):
    for x in range(0,9):
        collist.append(newlist[x][colno])
        print(newlist[x])
    print(collist)
    if collist.count("X") > 1:
        print("Wrong!")

grid()
print("Booyah")

newlist[2][1] = "X"
#newlist[2][2] = "X"
print(newlist[1])
print(newlist[2])
print(newlist)
#coloumncheck(2)
m.getch()
