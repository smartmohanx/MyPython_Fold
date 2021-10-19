import sqlite3
conn = sqlite3.connect("swar.db")
curs = conn.cursor()

data = curs.execute("select name,price from food_table")
print(list(data))