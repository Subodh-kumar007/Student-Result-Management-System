import sqlite3
from sqlite3 import Error
def show():
    try:
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        cur.execute("select * from employee")
        #cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows=cur.fetchall()
        for row in rows:
            print(row)
        con.close()
    except Error as ex:
        print(ex)

show()
