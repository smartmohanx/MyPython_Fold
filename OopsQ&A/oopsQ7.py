'''
10. Create a class called Customer with two methods
customertype() which displays the type of customer getPriviledge()
which displays the privileges according to type of the customer.
Create a class called CorporateCustomer which inherits the Customer
class and overides the methods given in the Customer class.
Create a class called PersonalCustomer which inherits the Customer
class and overides the methods given in the Customer class.
create another class called MainClass to execute the program.
'''

class Customer:
    def customertype(self,c_type,name,contact):
        self.c_type = c_type
        self.name = name
        self.contact = contact

    def getPriviledge(self):

        print("customer type is : ", self.c_type)
        print("customer name is : ", self.name)
        print("customer contact is : ", self.contact)

class CorporateCustomer(Customer):
    pass

class PersonalCustomer(Customer):
    pass

class MainClass:
    def cc(self,c_type,name,contact):
        print("==========================================")
        CorporateCustomer.customertype(self,c_type,name,contact)
        print("------DETAILS OF CORPORATE CUSTOMER-------")
        CorporateCustomer.getPriviledge(self)

    def pc(self,c_type,name,contact):
        print("==========================================")
        CorporateCustomer.customertype(self,c_type,name,contact)
        print("------DETAILS OF PERSONAL CUSTOMER-------")
        CorporateCustomer.getPriviledge(self)


print("WELCOME TO SMART-XTECH!")
print("CorporateCustomer type - 1\nPersonalCustomer type - 2")
c_type = int(input("Enter your customer type: "))
name = input("Enter your name: ")
contact = int(input("Enter your contact number:"))

obj1 = MainClass()

if c_type == 1:
    obj1.cc('CORPORATE CUSTOMER',name,contact)
if c_type == 2:
    obj1.pc('PERSONAL CUSTOMER',name,contact)