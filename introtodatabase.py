link = "https://www.quandl.com/api/v1/datasets/NUFORC/SIGHTINGS.xls?auth_token=mkRi3_Lz286wx87q8c5x"
import urllib.request
import xlrd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('DROP TABLE sightings')

c.execute('CREATE TABLE sightings (year text, month text, day text, cou text)')


urllib.request.urlretrieve(link, 'compiledata.xls')

wb = xlrd.open_workbook('compiledata.xls')

sh = wb.sheet_by_index(0)

cell = sh.cell(1,0)

cell = cell.value

for i in range(1,874):
    date = sh.cell(i,0)
    date = date.value
    date = xlrd.xldate_as_tuple(date,0)
    
    year = str(date[0])
    month = str(date[1])
    day = str(int(date[2]))
    count = sh.cell(i,1)
    count = str(int(count.value))
    
    s1 = "INSERT INTO sightings VALUES (" + year + "," + month + "," + day + "," + count + ")"
    c.execute(s1)
    conn.commit()
month = []
corres = []
for x in range(1,13):
    c.execute("SELECT COUNT(*) FROM sightings where month = " + str(x))
    corres.append(c.fetchall()[0][0])
    month.append(x)
##plt.plot(month,corres)
##plt.ylabel('Total Findings')
##plt.xlabel('Month')
##plt.show()

years = []
corres = []
for x in range(1,13):
    c.execute("SELECT cou FROM sightings where month = " + str(x))
    suma = 0
    alla = (c.fetchall())
    for item in alla:
        suma += int(item[0])
    corres.append(suma)
    years.append(x)
    

plt.plot(years,corres)
plt.ylabel('Total Findings')
plt.xlabel('Days')
plt.show()

    

   

