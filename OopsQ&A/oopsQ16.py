'''
20. Wap on Overriding Methods To implement Display method In
parent class and child class with same signature.
'''
class Parent:
    def title(self):
        print("i am your parent.")
        print("our title: SIGITI")
class Child(Parent):
    def title(self):
        Parent.title(self)
        print("i am your child :)")
obj = Child()
obj.title()