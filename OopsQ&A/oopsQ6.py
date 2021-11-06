'''
9.Create a class to store details of student like rollno, name,
course joined and fee paid so far. Assume courses are Core
Pyhon and Advance Python with course fees being 3000 and
3500.
Provide a constructor to take rollno, name and course. Provide the
following methods: Payment(amount) ,Print() ,DueAmount property,
Total Fee property
Add a static member to store Service Tax, which is set to 12.3%. Also
allow a property through which we can set and get service tax.
Modify Total Fee and Due Amount properties to consider service tax
'''


class Student:
    service_tax = 12.3  
    def __init__(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course

        print("your roll no:",self.rollno)
        print("your name:",self.name)
        print("your course:",self.course)

    def payment(self,amount):
        self.amount = amount
        print("Paid for",self.course,":",self.amount)

    def DueAmount(self):
        if self.course == 'CORE PYTHON':
            self.tax = ((3000-self.amount) * Student.service_tax)/100
            self.due_amount = 3000 - self.amount + self.tax
            print("Tax of available amount: ",self.tax)
            print("YOu have to pay Your due amount is:",self.due_amount)
        elif self.course == 'ADVANCE PYTHON':
            self.tax = ((3500-self.amount) * Student.service_tax)/100
            self.due_amount = 3500 - self.amount + self.tax
            print("Tax of available amount: ",self.tax)
            print("YOu have to pay Your due amount is:",self.due_amount)
    def Total_fee(self):
        print("--------------------------------------------")
        print("paid amount:",self.amount,"+ Tax with Due amount:",self.due_amount)
        print("Total fee:",self.amount + self.due_amount)  


print("WELCOME TO SMART-XTECH!")
print("PLEASE CHOOSE YOUR COURSE.\nA.CORE PYTHON code - 1\nB.ADVANCE PYTHON code - 2")
course = int(input("Enter your course code:"))
rollno = int(input("Enter your roll no:"))
name = input("Enter your name:")
pay = int(input("Enter your payment:"))
print("---------thanks for fillling this form------------")

if course == 1:
    obj = Student(rollno,name,'CORE PYTHON')
    obj.payment(pay)
    obj.DueAmount()
    obj.Total_fee()
elif course == 2:
    obj = Student(rollno,name,'ADVANCE PYTHON')
    obj.payment(pay)
    obj.DueAmount()
    obj.Total_fee()