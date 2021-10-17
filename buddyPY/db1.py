
import sqlite3

conn = sqlite3.connect("swar.db")

curs = conn.cursor() #purpose read and write.
#create a table
curs.execute("create table if not exists food_table(id_no INTEGER unique, name TEXT, quantity INTEGER, price INTEGER,total_price INTEGER)")

#insert values into a table:
id_no = int(input("food id no: "))
name = input("food name: ")
quantity = int(input("enter your food quantity: "))
price = int(input("price of each food: "))
total_price = quantity*price

curs.execute("insert into food_table values(?, ?, ?, ?, ?)",(id_no,name,quantity,price,total_price))







conn.commit() #saveD
conn.close()   

print('inserted successfully.')