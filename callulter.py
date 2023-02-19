import sqlite3
import math
def connect():

    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREAT TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,yeaer INT)")
    conn.commit()
    conn.close()

x="hellow my mom"
print(5 != 6)
print(math.pow(2, 3))
print(2^3)

a={1,2,3,4,5}
a.add(5)
a.add(6)
print(a)

{x :x*x for x in range(1,100)}