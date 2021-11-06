#example of Hierarchical inheritance

class Parent:
    def parent_properties(self):
        print("i am parent.")
        print("Title:python")

class Child1(Parent):
    def child_prop(self):
        print("i am child 1.")

class Child2(Parent):
    def child_prop(self):
        Parent.parent_properties(self)
        print("i am child 2.")

class Child3(Parent):
    def child_prop(self):
        print("i am child 3.")

obj = Child2()
obj.child_prop()