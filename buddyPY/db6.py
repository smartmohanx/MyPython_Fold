# import sqlite3

# conn = sqlite3.connect("swar.db")

# curs = conn.cursor()

# #create a new table
# curs.execute("create table if not exists new_table(id_no INTEGER unique, name TEXT, quantity INTEGER, price INTEGER,total_price INTEGER)")


# conn.commit() #saveD
# conn.close()   

# print('created successfully.')



import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor()

curs.execute("insert into new_table SELECT id_no,name,quantity,price,total_price FROM food_table")

conn.commit()
conn.close()