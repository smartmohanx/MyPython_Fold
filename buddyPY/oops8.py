#hybrid inheritance Example.

class Parent:
    def title(self):
        print("TITLE:GOPPILI")

class Child1(Parent):
    def name_1(self):
        print("NAME: FATHER")

class Child2(Parent):
    def name_2(self):
        print("NAME: UNCLE")

class Grand_child(Child1,Child2):
    def name_12(self):
        Parent.title(self)
        Child1.name_1(self)
        print("Grand_child name.")

obj = Grand_child()
obj.name_12()