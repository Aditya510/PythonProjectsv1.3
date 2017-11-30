import os
import sqlite3
import time

#pathname
path = "C:\\Users\\Aditya\\Downloads\\brown"
filenames = (os.listdir(path))
path += "\\"

#mysql initilization
conn = sqlite3.connect('word.db')
c = conn.cursor()
c.execute("DROP TABLE WORDS")
c.execute("CREATE TABLE WORDS (word text, app int)")

#timer and counter
start = time.time()
counter = 0

for filename in filenames:

    file = open(path+filename, "r")

    #timer and counter
    current = time.time()
    print(current - start)
    counter += 1
    print(counter)
    print(file)
    #build data
    for line in file:
        print(line)
        for item in line.split():
            item = item[:item.index("/")]
            if item.isalpha():
                
                
                s = "SELECT app from words where word = '" + str(item) + "'"
                c.execute(s)
                
                count = c.fetchall()
                #append new word
                if len(str(count)) == 2:
                    s = "INSERT INTO WORDS VALUES ('" + str(item) + "',1)"
                    
                    c.execute(s)
                #edit value if exists
                else:
                    
                    count = count[0][0]
                    
                    count += 1
                    s = "UPDATE WORDS SET app = " + str(count) + " WHERE word = '" + item + "'"
                    
                    c.execute(s)


c.execute("SELECT word from WORDS where word = 'the'")
print(c.fetchall())
