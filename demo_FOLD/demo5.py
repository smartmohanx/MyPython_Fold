# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

class Animal(ABC):
    # in this class,
    # if only one method is avaible then,
    # no need to write decorator.

    #@abstractmethod 
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("human: I can walk and run")

class Snake(Animal):
    def move(self):
        print("Snake: I can crawl")

class Dog(Animal):
    def move(self):
        print("Dog: I can bark")

class Lion(Animal):
    def move(self):
        print("Lion: I can roar")

# Driver code
H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()
