'''
18. Create a class to Calculate Employee Total Salary Accept Basic
Salary, DA, HRA from keyboard If Employee Salary Greater Then
20,000 Then increment 20% of salary and Display Total Salary;
overriding:
'''
class Employee:
    def __init__(self,basic,da,hra):
        self.basic = basic
        self.da = da
        self.hra = hra

    def display(self):
        self.total = self.basic + self.da + self.hra
        print("(basic:",self.basic,")+(","da:",self.da,")+(","hra:",self.hra,")")
        print("Total Salary:",self.total)

class SalaryCal(Employee):
    def display(self):
        Employee.display(self)
        if self.total > 20000:
            self.sal_i = (self.total * 20)/100
            print("Increments Amount:",self.sal_i)
            self.total_inc = (self.total) + self.sal_i
            print("Total Salary with increment(20%):",self.total_inc)
print("WELCOME TO SMART-XTECH!")
print("PLEASE PROVIDE DETAILS BELOW:")
basic = int(input("ENTER YOUR BASIC SALARY:"))
da = int(input("ENTER YOUR DA SALARY:"))
hra = int(input("ENTER YOUR HRA SALARY:"))
obj = SalaryCal(basic,da,hra)
obj.display()