import sqlite3
conn = sqlite3.connect("swar.db")
curs = conn.cursor()

'''
#fetching_all data from table

curs.execute("select * from food_table")

records = curs.fetchall()
for row in records:
    print('id_no:',row[0])
    print('name:',row[1])
    print('quantity:',row[2])
    print('price:',row[3])
    print("total price:",row[4])
    print("discount:",row[5])

#print(records)

#fetching one data.
'''
id_no = int(input("enter your idno:"))
curs.execute("select * from food_table where id_no = ?",(id_no,))
record = curs.fetchone()
print(record)
