#deleting column in table.
#actually we can't delete column in table but
#we can copy all data from old(TABLE) to NEW(TABLE) CREATED ONE.

import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

#NEW TABLE
curs.execute("create table if not exists FOOD(id_no integer unique,name TEXT,quantity integer,price integer,total_price integer)")
#Copying from old to new.
curs.execute("insert into FOOD SELECT id_no,name,quantity,price,total_price FROM food_table")


conn.commit()
conn.close()
