#how to update table in database.

import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

id = int(input("enter your id no: "))
price = int(input("enter your udpated price: "))

curs.execute("UPDATE food_table set price = ? where id_no = ?",(price,id))

conn.commit()
conn.close()
