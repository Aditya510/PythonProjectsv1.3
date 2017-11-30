
import sqlite3

file = open("C:\\Users\\Aditya\\Documents\\AITS.txt", "r")
conn = sqlite3.connect('aits.db')
c = conn.cursor()
c.execute("DROP TABLE AITS4")
c.execute("CREATE TABLE AITS4 (chem int, phy int, math int, total int, rank int)")
for line in file:
    items = line.split(",")
    
    query = "INSERT INTO AITS4 VALUES ("
    query += items[0] + ',' + items[1] + ',' + items[2] + ',' + items[3] + ',' + items[4] + ')'
    c.execute(query)


import matplotlib.pyplot as plt
c.execute("SELECT total,rank,chem,phy,math from aits4")
lisa = c.fetchall()
marks = []
rank = []
phy = []
math = []
chem =[]
for item in lisa:
    marks.append(item[0])
    rank.append(item[1])
    chem.append(item[2])
    phy.append(item[3])
    math.append(item[4])
##plt.plot(rank,marks)
##
##
##plt.show()
##plt.plot(rank,math)
##plt.plot(rank,phy)
##plt.show()
marks = []
occur = []
for i in range(-41,195):
    query = "SELECT COUNT(*) from aits4 where total =" + str(i)
    c.execute(query)
    marks.append(i)
    occur.append(c.fetchall()[0][0])
print(marks,occur)
plt.plot(marks,occur)
plt.show()
