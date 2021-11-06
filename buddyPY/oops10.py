#overloading

class Name:
    def call(self,name = None):

        if name is not None:
            self.name = name
            print("hello " + self.name)
        else:
            print("hello")

obj = Name()

obj.call('swar')
obj.call()
obj.call('mohan')