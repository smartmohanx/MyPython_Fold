import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor()

#insert values into a table:
id_no = int(input("food id no: "))
name = input("food name: ")
quantity = int(input("enter your food quantity: "))
price = int(input("price of each food: "))
total_price = quantity*price

curs.execute("insert into food_table values(?,?,?,?,?)",(id_no,name,quantity,price,total_price))

conn.commit()
conn.close()

print("inserted successfully.")