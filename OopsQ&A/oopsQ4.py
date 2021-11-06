'''
7. Consider the following scenario:
A Furniture Manufacturer manufactures domestic furniture.
Customers provide their specifications to the company for the
furniture they want. To cope up with the received customer's order,
FFC decides to computerize the order-processing system. The System
should accept the values of furniture items, such as a bookshelf and
a chair. You need to develop the hierarchy of these items.
'''

#Hierarchical inheritance.
class furniture:

    def __init__(self,custom_name,contact,furn_name,metal,design):
        self.custom_name = custom_name
        self.contact = contact
        self.furn_name = furn_name
        self.metal = metal
        self.design = design
    
    def display_details(self):
        print("your name:", self.custom_name)
        print("your contact number:",self.contact)
        print("your chosen furniture name:",self.furn_name)
        print("furniture metal is:",self.metal)
        print("And it's design:",self.design)

class bookshelf(furniture):
    def bookshelf_details(self):
        furniture.display_details(self)
        print("Dear Customer!")
        print("WORKING DAYS: It takes 10-15days to complete.")
        print("And It's price: 7000/- only")
        print("THANKS FOR CHOOSING US.")

class chair(furniture):
    def chair_details(self):
        furniture.display_details(self)
        print("WORKING DAYS: It takes 7-10days to complete.")
        print("And It's price: 3000/- only")
        print("THANKS FOR CHOOSING US.")

print("Customer should have to fill this below form;")
name = input("A).enter you name:")
contact = int(input("B).enter your contact:"))
furniture_name = input("C).1.bookshelf or 2.chair (1/2):")
metal = input("D).enter your metal:")
design = input("E).enter your design name:")


if furniture_name == "1":
    print("\n---------thanks for giving details------------\n")
    obj1 = bookshelf(name,contact,'BOOKSHELF',metal,design)
    obj1.bookshelf_details()

elif furniture_name == '2':
    print("\n---------thanks for giving details------------\n")
    obj2 = chair(name,contact,'CHAIR',metal,design)
    obj2.chair_details()
    
else:
    print("\nPLEASE ENTER 1 OR 2 (only) IN C) field.")







# #mulit-level inheritance.
# class furniture:

#     def sofa(self):
#         print("you selected sofa.")
#     def chair(self):
#         print("you selected chair.")
#     def table(self):
#         print("you selected table.")

# class values(furniture):

#     def sofa_value(self):
#         furniture.sofa(self)
#         print("And it's price approx. 15000/-")
#     def chair_value(self):
#         furniture.chair(self)
#         print("And it's price approx. 7000/-")
#     def table_value(self):
#         furniture.table(self)
#         print("And it's price approx. 10000/-")


# class full_details(furniture):

#     def sofa(self):
#         values.sofa_value(self)

#     def chair(self):
#         furniture.chair_value(self)

#     def table(self):
#         furniture.table_value(self)

# print("Available furniture items are given below,\nthese should be made for you.")
# print("1.sofa,2.chair,3.table")

# x = (input("enter here: "))


# obj1 = full_details()

# if x == '1':
#     obj1.sofa()
    
# elif x == '2':
#     obj1.chair()

# elif x == '3':
#     obj1.table()

# elif x == '1,2' or '2,1' or '1 2' or '2 1':
#     obj1.sofa()
#     obj1.chair()
# elif x == '1,3' or '1 3' or '3,1' or '3 1':
#     obj1.sofa()
#     obj1.table_()

# elif x == '2,3' or '3,2' or '3 2' or '2 3':
#     obj1.chair()
#     obj1.table_()