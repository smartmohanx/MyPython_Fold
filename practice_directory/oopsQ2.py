
'''
5. Create a reference type called Person. Populate the Person
class with the following attributes to store the following
information: First name, Last name, Email address, Date of
birth Add constructors that accept the following parameter
lists: All four parameters First name , Last name , Email ,First
name , Last name , Date of birth
write appropriate methods to accept and display the details.
'''

import sqlite3
conn = sqlite3.connect("mohanX.db")
curs = conn.cursor()



class Person:
    def __init__(self,first_name,last_name,email,dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
    def display_details(self):
        print("--------------------------------------")
        print("First name of Person: ",self.first_name)
        print("Last name of Person: ",self.last_name)
        print("His/Her Email: ",self.email)
        print("Date of birth: ",self.dob)

fname = input("enter your first name: ")
lname = input("enter your last name: ")
email = input("enter your email: ")
dob = input("enter your date of birth: ")

ob = Person(fname,lname,email,dob)
ob.display_details()



curs.execute("create table if not exists Person_emp(fname integer,lname integer,email text unique,dob text)")

curs.execute("insert into Person_emp values(?,?,?,?)",(fname,lname,email,dob))

conn.commit()
conn.close()

print("done.........!!")