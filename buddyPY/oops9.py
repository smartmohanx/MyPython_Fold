#polymerphism example:

class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

 # common interface function
def flying_test(bird):
    bird.fly()

def swim_test(bird):
    bird.swim()

#objects creation
par = Parrot()
peng = Penguin()

# passing the object
flying_test(par)
flying_test(peng)

swim_test(par)
swim_test(peng)