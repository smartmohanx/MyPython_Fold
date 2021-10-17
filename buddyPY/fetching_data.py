
#fetching data from table.

import sqlite3

conn = sqlite3.connect("extra.db")

curs = conn.cursor() #purpose read and write.


#fetching_all
'''
curs.execute("select * from food_table")
records = curs.fetchall()
print(records)

for i in records:
    print(i)
'''


#fetch_one
'''
id_no = int(input("ENTER YOUR ID NO: "))
curs.execute("select * from food_table where id_no = ?",(id_no,))
records = curs.fetchone()
print(records)
'''
