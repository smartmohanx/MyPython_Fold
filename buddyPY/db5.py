import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.

#insert values into a table:
id_no = int(input("food id no: "))
name = input("food name: ")
quantity = int(input("enter your food quantity: "))
price = int(input("price of each food: "))
total_price = quantity*price
disc = int(input("enter discount in percentage: "))

curs.execute("insert into food_table values(?,?,?,?,?,?)",(id_no,name,quantity,price,total_price,disc))

conn.commit()
conn.close()
