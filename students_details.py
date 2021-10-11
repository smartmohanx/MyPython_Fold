class students:
    def assign_details(self,rollno,name,village,gender,dob=None,age=0,caste=None):
        self.roll = rollno
        self.name = name
        self.dob = dob
        self.village = village
        self.gender = gender
        self.age = age
        self.caste = caste
    
    def show_details(self):
        print("roll number:",self.roll)
        print("name:",self.name)
        print("village:",self.village)
        print("gender:",self.gender)
        print("date of birth:",self.dob)
        print("age:",self.age)
        print("caste:",self.caste)

roll_no = int(input("enter your roll number: "))
name = input('enter your name: ')
village = input("enter your village name: ")
gender = input("enter your gender: ")
dob = input("enter your date of birth: ")
age = int(input("enter your age: "))
caste = input("enter your caste: ")

stud = students()

# stud1 = stud.assign_details(121,'mohan','newbaxipalli','male','april1')
# stud_1 = stud.show_details()

# print("===========================")

# stud2 = stud.assign_details(122,'swar','venkatraipur','male','march4',23)
# stud_2 = stud.show_details()

# print("===========================")

if dob == 'x':
    dob = "skipped"
if caste == 'x':
    case = "skipped"

stud1 = stud.assign_details(roll_no,name,village,gender,dob,age,caste)
stud_1 = stud.show_details()
#ji
#mohan 
