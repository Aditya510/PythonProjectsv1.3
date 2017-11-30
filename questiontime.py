import time
import sqlite3
import datetime
conn = sqlite3.connect("time.db")
c = conn.cursor()
c.execute("DROP TABLE QUESTIONS")
c.execute("CREATE TABLE QUESTIONS (time int primary key, sub varchar(10),chap varchar(100))")

target = 66

while True:
    load = input("Waiting... ,'cb' for subject change ")
    subject  = ""
    if load == 'cb':
        subject = input("Enter 'p','c','m'").lower()
        chapter = input("Enter chapter name")
    if subject == 'p':
        subject = "Physics"
    elif subject == 'm':
        subject = "Mathematics"
    elif subject == 'c':
        subject = "Chemistry"
    
    
    tim = (time.time())
    tim= int(tim)
    try:
        c.execute("INSERT INTO QUESTIONS  VALUES (%d , '%s', '%s')" % (tim, subject, chapter))
    except:
        print("No double entries!")
    
    c.execute("SELECT count(*) FROM QUESTIONS")
    print(c.fetchall()[0][0])
    

