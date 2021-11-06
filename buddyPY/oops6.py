#Example of multilevel inheritance

class A:
    def add(self):
        return 5+5 #output - 10
class B(A):
    def sub(self):
        return 5-2 #output - 3
class C(B):
    def multi(self):
        return 5*3 #output - 15

obj = C()
print(obj.sub())
print(obj.add())
print(obj.multi())