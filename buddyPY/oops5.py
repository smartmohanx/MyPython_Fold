#example of multiple inheritance
class Parent_1:
    def __init__(self):
        print("i am Constructor from P1.")
    def add(self):
        print("i am add method")
class Parent_2:
    def __init__(self):
        print("i am Constructor from P2.")

class Child(Parent_1,Parent_2):
    def __init__(self):
        Parent_2.__init__(self)

obj = Child()
