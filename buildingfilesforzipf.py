#buildfiles
import os
import sqlite3
import time

###pathname
##path = "C:\\Users\\Aditya\\Downloads\\brown\\brown"
##filenames = (os.listdir(path))
##path += "\\"
##
##newfile = open("combination.txt", "w")
##
##for filename in filenames:
##    
##    file = open(path+filename, "r")
##    for line in file:
##        newfile.write(line)

#timer and counter

##counter = 0
##
##file = open("combination.txt","r")
##    #timer and counter
##
##
##
##counta = 0
##wordlist = []
##countlist = []
###build data
##for line in file:
##    counta+=1
##    if counta % 10000 == 0:
##        print(counta)
##    
##    
##    for item in line.split():
##        item = item[:item.index("/")]
##        
##        if item.isalpha():
##              item = item.lower()
##              if item in wordlist:
##                  index = wordlist.index(item)
##                  countlist[index] = countlist[index] + 1
##              else:
##                  wordlist.append(item)
##                  countlist.append(1)
##result = open("result.txt","w")
##result.write(str(countlist))
countlist = []
result = open("result.txt",'r')
for line in result:
              line = line[1:]
              line = line[:-1]
              line = line.split(",")
              
              for item in line:
                  
                  countlist.append(int(item))

countlist.sort()
simullist= []

import matplotlib.pyplot as plt
countlist = countlist[::-1]
countlist = countlist[:10000]
emplist = list(range(0,len(countlist)))

plt.plot(emplist,countlist)
for i in range(0,len(countlist)):
    simullist.append(countlist[0]/(i+1))
plt.plot(emplist, simullist)
plt.show()



