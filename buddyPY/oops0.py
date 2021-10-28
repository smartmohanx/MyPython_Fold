
class parent:  #class

    name = "python"
    teaching = "mohanx"   #static variables

    @staticmethod
    def sum():   #static method
        print("add:",10+30)

    def add(self): #instance method

        self.a = 10  
        self.b = 20 #instance variables
        print("i am add method.")

#calling static method
parent.sum()