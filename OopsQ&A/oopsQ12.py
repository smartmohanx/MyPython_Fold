'''
17. Create a class to implement calculate simple and compound
interest using method find interest method.
'''

class Calculator:
    def simple_interest(self,p,t,r):
        self.p = p
        self.t = t
        self.r = r
        self.s_i = (self.p * self.t * self.r)/100
        self.total_amount = self.p + self.s_i
        print("Principle amount:",self.p)
        print("Time in years:",self.t)
        print("Rate of interest:",self.r)
        print("Total Simple interest Amount:", self.s_i)
        print("Final Amount:", self.total_amount)

    def compound_interest(self,p,t,r,n):
        self.p = p
        self.t = t
        self.r = r/100
        self.n = n
        self.pow = self.t * self.n
        self.c_i = (self.p * (1 + self.r/self.n)**self.pow)
        self.total_amount = (self.p + self.c_i)
        print("Principle amount:",self.p)
        print("Time in years:",self.t)
        print("Rate of interest:",self.r)
        print("No of times interest applied:",self.n)
        print("Total compound interest Amount:", self.c_i)
        print("Final Amount:", self.total_amount)

print("WELCOME TO SMART-XTECH!")
x = int(input(("CHOOSE SIMPLE INTEREST = 1\nOR COMPOUND INTEREST = 2\n:")))

if x == 1:
    p = int(input("Enter Principle amount:"))
    t = int(input("Enter time in years:"))
    r = float(input("Enter rate of interest:"))
    obj = Calculator()
    obj.simple_interest(p,t,r)
elif x == 2:
    p = int(input("Enter Principle amount:"))
    t = int(input("Enter time in years:"))
    r = float(input("Enter rate of interest:"))
    n = int(input("No of times interest applied:"))
    obj = Calculator()
    obj.compound_interest(p,t,r,n)