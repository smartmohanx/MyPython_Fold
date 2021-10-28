#!/usr/bin/env python
class Person:
    def Hello(self, name=None):
        if name is not None:
                print('Hello ' + name)
        else:
            print('Hello ')
# Create instance
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Edureka')