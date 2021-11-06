#single inheritance example;

#parent class
class Parent:
    def title(self):
        print("TITLE:GOPPILI")
        print("i am parent class.")
#child class
class Child(Parent):
    def details(self):
        print("i am child class")

obj = Child()
obj.details()
obj.title()