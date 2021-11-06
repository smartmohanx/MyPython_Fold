'''4. For an Online Bookstore create a class to store book details
and display the book details with fields are book number,
book name, book title, book author, quantity of books, book
price. calculate and display the bill amount .'''

import sqlite3
conn = sqlite3.connect("mohanX.db")
curs = conn.cursor()


class bookStore:
    def book_details(self,b_no,b_name,b_title,b_author,b_quantity,b_price):
        self.b_no = b_no
        self.b_name = b_name
        self.b_title = b_title
        self.b_author = b_author
        self.b_quantity = b_quantity
        self.b_price = b_price

    def show_book_details(self):
        print('---------------------------------')
        print('book number is: ',self.b_no)
        print('book name is: ',self.b_name)
        print('book title is: ',self.b_title)
        print('book author is: ',self.b_author)
        print('book quantity : ',self.b_quantity)
        print('book price is: ',self.b_price)
        print('The total price of book: ',total_price)


b_no = int(input("enter your book number: "))
b_name = input("enter your book name: ")
b_title = input("enter your book title: ")
b_author = input("enter your author name: ")
b_quantity = int(input('enter your book quantity: '))
b_price = int(input("enter your book price: "))
total_price = b_quantity * b_price

f_obj1 = bookStore()
f_obj1.book_details(b_no,b_name,b_title,b_author,b_quantity,b_price)
f_obj1.show_book_details()

curs.execute("create table if not exists STOREBOOK(b_no integer unique,b_name text unique,b_title text unique,b_author text,b_quantity integer,b_price integer,total_price integer)")

curs.execute("insert into STOREBOOK values(?,?,?,?,?,?,?)",(b_no,b_name,b_title,b_author,b_quantity,b_price,total_price))

conn.commit()
conn.close()

print("done.........!!")