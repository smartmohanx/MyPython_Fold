import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor()

id_no = int(input("ENTER YOUR ID NO: "))
curs.execute("delete from FOOD where id_no = ?",(id_no,))

conn.commit()
conn.close()

print("deleted successfully:", id_no)