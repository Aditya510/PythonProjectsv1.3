#Minesweeping

import random

def randomnum(grid):
    gridsize = len(grid)
    x = random.randint(0,gridsize-1)
    y = random.randint(0, gridsize-1)
    return (x,y)

def getneighbours(grid,x,y):
    neighbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            elif (x+i) > len(grid)-1 or (y+j) > len(grid)-1:
                continue
            elif (x+i)< 0 or (y+j) < 0:
                continue
            neighbours.append((x+i,y+j))
    return neighbours

def generatemines(grid, start, numberofmines):
    mines = []
    while len(mines) < numberofmines:
        mine = randomnum(grid)
        if mine == start or mine in getneighbours(grid, start[0] , start[1]) or mine in mines:
            continue
        mines.append(mine)
    
    return mines

def getcount(grid):
    for i in range(0,len(grid) ):
        for j in range(0,len(grid)):
            if grid[i][j] == "X":
                continue
            values = getneighbours(grid,i,j)
            count = 0
            for item in values:
                if grid[item[0]][item[1]] == "X":
                    count +=1
            grid[i][j] = count
    return grid

def expose(overboard,underboard,x,y):
    if overboard[x][y] != " ":
        return 
    overboard[x][y] = underboard[x][y]
    5
    if underboard[x][y] == 0:
        for item in getneighbours(underboard,x,y):
            if underboard[item[0]][item[1]] != "X":
                expose(overboard,underboard,item[0],item[1])


underboard=  [[" "]*9 for i in range(0,9)]
overboard = [[" "]*9 for i in range(0,9)]


x = 2
y = 3

start = (x,y)

mines = generatemines(underboard, start , 10)
for item in mines:
    underboard[item[0]][item[1]] = "X"
underboard= getcount(underboard)
##print(underboard)
expose(overboard,underboard,x,y)
##for item in overboard:
##    print(item)

#######################################################################################

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
redbutton = Button(frame, text="Red", fg="red")
def f(x):
    print("Hello world")
    print(x)
redbutton.bind('<Button-3>',f)
redbutton.pack( side = LEFT)

root.mainloop()
