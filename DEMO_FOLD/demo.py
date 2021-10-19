import sqlite3
conn = sqlite3.connect("mohanx.db")
curs = conn.cursor()

curs.execute("create table if not exists mytable(id_no integer unique,name TEXT, salary integer)")

#curs.execute("insert into mytable values(101,'mohanx',10000)")

#curs.execute("insert into mytable values(102,'swar',20000)")

id = int(input("enter your id:"))
sal = int(input("enter your salary:"))

curs.execute("update mytable set salary = ? where id_no = ?",(sal,id))

conn.commit()
conn.close()