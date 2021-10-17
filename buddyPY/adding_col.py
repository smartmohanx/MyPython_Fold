#SQL -> stands for structure query language.
#adding extra column in table

import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

curs.execute("ALTER TABLE food_table ADD discount integer")

conn.commit() #saveD
conn.close()   
