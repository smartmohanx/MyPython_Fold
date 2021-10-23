class student:
    def assign(self,rollno,name,eng,math,sc):
        self.rollno = rollno
        self.name = name
        self.eng = eng
        self.math = math
        self.sc = sc
    def display(self):
        total_marks = self.eng + self.math + self.sc
        percent_marks = total_marks/3
        print("name:",self.name)
        print("total marks:",total_marks)
        print("percent of total marks:",percent_marks)

ob = student()
ob.assign(101,'mohan',49,80,67)
ob.display()

ob.assign(102,'swar',50,38,60)
ob.display()