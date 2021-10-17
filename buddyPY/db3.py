#SQL -> stands for structure query language.

#how to delete table from database.

import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

curs.execute("drop table if exists food_table")

conn.commit()
conn.close()