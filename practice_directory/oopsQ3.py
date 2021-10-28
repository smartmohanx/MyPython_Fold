'''
6.case study:
Yatra.Com Travels is a committed tour and travel company. It has
devised many innovative packages for its customers who want to
take a holiday. There are three kinds of tours:
a)Discover India b)Holiday Hungama c)Pilgrimage Package
These tours start every week. A customer can avail of a package
belonging to any category, starting on any given date. The customer
can also specify the number of people accompanying the customer.
The customer class will have the following member data: customer
name, number of people accompanying(int), package
category(D/H/P), cost(float), tour start date
Write an executable program with

'''
import sqlite3
conn = sqlite3.connect("mohanX.db")
curs = conn.cursor()





class Customer:
    print("============\n YATRA.COM \n============")
    def __init__(self,name,no_people,package_cat,cost,t_date):
        self.name = name
        self.no_people = no_people
        self.package_cat = package_cat
        self.cost = cost
        self.t_date = t_date

    def display_details(self):
        print("customer name: ",self.name)
        print("Number of people: ",self.no_people)
        print("Package category(D/H/P): ",self.package_cat)
        
        print("cost of customer: ",self.cost)
        print("Starting Date: ",self.t_date)
        print("Total bill amount of customer:",total_bill)

name = input("enter your name: ")
no_people = int(input("enter your number of people: "))
package_cat = input("enter your packge category(D/H/P): ")
cost = float(input("enter your cost: "))
date = input("enter your date: ")
total_bill = no_people * cost


ob = Customer(name,no_people,package_cat,cost,date)
ob.display_details()



curs.execute("create table if not exists TRAVEL_TOUR(name integer,no_people integer,package_cat text,cost real,date text,total_bill real)")

curs.execute("insert into TRAVEL_TOUR values(?,?,?,?,?,?)",(name,no_people,package_cat,cost,date,total_bill))

conn.commit()
conn.close()

print("done.........!!")