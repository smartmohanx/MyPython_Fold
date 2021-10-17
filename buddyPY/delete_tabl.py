import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

curs.execute("DROP TABLE IF EXISTS food_table")

conn.commit()
conn.close()
print("table is deleted if it exists.")