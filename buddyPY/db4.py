import sqlite3
conn = sqlite3.connect("swar.db")
curs = conn.cursor()

#fetching_all data from table
'''
curs.execute("select * from food_table")

records = curs.fetchall()

#print(records)

for i in records:
    print(i[1])
'''
#fetching one data.
'''
id_no = int(input("enter your idno:"))
curs.execute("select * from food_table where id_no = ?",(id_no,))
record = curs.fetchone()
print(record)
'''
#summary>?