
import psycopg2 as pg2
conn = pg2.connect(database='dvdrental',user='postgres',password='pass')
cur=conn.cursor()
cur.execute("SELECT * FROM payment")
#returns tuble of the first row as python object
cur.fetchone()
#return n no of roots
cur.fetchmany(10)
#returns all rows at once
cur.fetchall()
#to save and index results,assign it to variable
data=cur.fetchmany(10)

conn.close()
