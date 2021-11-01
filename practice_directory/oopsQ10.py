'''
13.
Create a base class, Telephone, and derive a class
Electronic Phone from it. In Telephone, create a protected
string member phonetype, and a public method Ring( ) that
outputs a text message like this: "Ringing the <phonetype>." In
ElectronicPhone, the constructor should set the phonetype to
"Digital." In the Run( ) method, call Ring( ) on the Electronic
Phone to test the inheritance?
'''
class Telephone:
    _phonetype = 'normal-phone'
    def Ring(self):
        print("Ringing the",self._phonetype)

class ElectronicPhone(Telephone):
    def __init__(self):
        _phonetype = "Digital"
        print(self._phonetype)
    def Run(self):
        Telephone.Ring(self)
        
obj = ElectronicPhone()
obj.Run()
