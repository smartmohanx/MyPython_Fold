'''

11.
Write an executable program.
Create a class Shape with the following methods
getDetails() to get details from the user 
calculateArea() to calculate the area with the given dimensions
displayDetails() to display the calculated area of the shape.
Create a class called Triangle which inherits Shape class and provides
appropriate implementation of the methods given in the base class.
Create a class called circle which inherits Shape class and provides
appropriate implementation of the methods given in the base class.

'''


class Shape:
    def getDetails(self,id,name,shape,side_a=None,side_b=None,side_c=None,r=None):
        self.id = id
        self.name = name
        self.shape = shape
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.r = r

    def calculateArea(self):
        if self.shape == 'TRIANGLE':
            self.area = (self.side_a * self.side_b)/2
        elif self.shape == "CIRCLE":
            self.area = 3.14 * (self.r)**2

    def displayDetails(self):
        Shape.calculateArea(self)
        print("YOUR ID:",self.id)
        print("YOUR NAME:",self.name)
        print("YOUR RADIUS:",self.r)
        print("YOUR LENGHT:",self.side_a)
        print("YOUR WIDTH:",self.side_b)
        print("AREA OF CALCULATED RESULT:",self.area)


class Triangle(Shape):
    def ts(self):
        Shape.displayDetails(self)

class Circle(Shape):
    def cs(self):
        Shape.displayDetails(self)
    

print("WELCOME TO SMART-XTECH!")
print("CALCULATE'S AREA OF SHAPE;")
print("A). TRIANGLE code - 1\nB). CIRCLE code - 2")

shape = int(input("Shape code:"))

if shape == 1:
    id = int(input("Enter Your id: "))
    name = input("Enter Your name: ")
    a = int(input("Enter Length:"))
    b = int(input("Enter Width:"))
    obj1 = Triangle()
    obj1.getDetails(id,name,'TRIANGLE',a,b)
    obj1.ts()

elif shape == 2:
    id = int(input("Enter Your id: "))
    name = input("Enter Your name: ")
    r = int(input("Enter Radius:"))
    obj2 = Circle()
    obj2.getDetails(id,name,'CIRCLE',r=r)
    print("----YOUR CIRCLE DETAILS----")
    obj2.cs()