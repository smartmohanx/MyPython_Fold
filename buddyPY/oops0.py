
class parent:  #class

    def instance_var(self,a,b):  #instance method
        self.a = a  
        self.b = b  #instance variables

    def display(self):  #instance method
        print("first instance variable:",self.a)
        print("second instance variable:",self.b)
    
    def add(self):   #instance method
        sum = self.a + self.b
        print("sum:",sum)

#creating object
obj = parent()
#calling instance variables
obj.instance_var(10,20)
#callling methods
obj.display()
obj.add()