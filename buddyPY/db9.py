import sqlite3
conn = sqlite3.connect("swar.db")
curs = conn.cursor()

curs.execute("alter table item_table drop name")

conn.commit()
conn.close()