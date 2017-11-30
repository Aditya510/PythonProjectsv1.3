file = open("tesla1.csv", "r")
import sqlite3
import matplotlib.pyplot as plt
conn = sqlite3.connect('stock.db')
c = conn.cursor()
####c.execute('DROP TABLE TESLA')
##c.execute('CREATE TABLE TESLA (day text, month text, year text, opens text, high text, low text, close text)')
##          
##for line in file:
##    
##    point = line.split(",")
##    date = point[0]
##    year = date[:2]
##    month = date[3:5]
##    day = date[6:10]
##    opens = point[1]
##    high = point[2]
##    low = point[3]
##    close = point[4]
##    insertquery = "INSERT INTO TESLA VALUES (" + year + "," + month + "," + day + "," + opens + "," + high + "," + low + "," + close + ")"
##    
##    c.execute(insertquery)
##    conn.commit()


month = []
corres = []

c.execute("SELECT close FROM tesla")
suma = 0
alla = (c.fetchall())

for item in alla:
    
    corres.append(float(item[0]))
    month.append(suma)
    suma += 1
    
corres = corres[::-1]
plt.plot(month,corres)
plt.ylabel('Total Findings')
plt.xlabel('Days')
plt.show()
