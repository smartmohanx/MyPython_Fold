'''
8. Create the classes required to store data regarding different
types of Courses. All courses have name, duration and course
fee. Some courses are part time where you have to store the
timing for course. Some courses are onsite where you have to
store the company name and the no. of candidates for the
course. For onsite course we charge 10% more on the course
fee. For part-time course, we offer 10% discount.

Provide constructors and the following methods.
Print()
GetTotalFee()
'''



class python:
    def __init__(self):
        print("course name: PYTHON")
        print("Duration of course: 60days")
        print("Timing: EVERYDAY AT 11AM(1hr)")
    def GetTotalFee(self):
        print("Course fees: 5000/-rs only")
        self.extra_discount = 5000 - 5000*10/100
        print("Total course fees(including discount):",self.extra_discount)
class java:
    def __init__(self):
        print("course name: JAVA")
        print("Duration of course: 50days")
        print("Timing: EVERYDAY AT 11AM(1hr)")
    def GetTotalFee(self):
        print("Course fees: 5000/-rs only")
        self.extra_discount = 5000 - 5000*10/100
        print("Total course fees(including discount):",self.extra_discount)
class ruby:
    def __init__(self):
        print("Company name: SmartX-tech")
        print("No. of candidates can be joined: 25 students only")
        print("course name: RUBY")
        print("Duration of course: 50days")
        print("Timing: EVERYDAY AT 11AM(1hr)")
    def GetTotalFee(self):
        print("Course fees: 15000/-rs only")
        self.extra_charges = 15000 + 15000*10/100
        print("Total course fees(including extra charges):",self.extra_charges)
    
class django:
    def __init__(self):
        print("course name: DJANGO")
        print("Duration of course: 45days")
        print("Timing: EVERYDAY AT 11AM(1hr)")
    def GetTotalFee(self):
        print("Course fees: 5000/-rs only")
        self.extra_discount = 5000 - 5000*10/100
        print("Total course fees(including discount):",self.extra_discount)



print("Courses of list")
print("A.PYTHON code - 1\nB.JAVA code - 2\nC.RUBY code - 3\nD.DJANGO code - 4")
INPUT = int(input("Enter your course code:"))

if INPUT == 1:
    print("--------DETAILS COURSE---------")
    obj = python()
    obj.GetTotalFee()
elif INPUT == 2:
    print("--------DETAILS COURSE---------")
    obj = java()
    obj.java_course()
elif INPUT == 3:
    print("--------DETAILS COURSE---------")
    obj = ruby()
    obj.ruby_course()
elif INPUT == 4:
    print("--------DETAILS COURSE---------")
    obj = django()
    obj.GetTotalFee()