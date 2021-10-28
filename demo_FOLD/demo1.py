# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def no_of_sides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def no_of_sides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def no_of_sides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def no_of_sides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def no_of_sides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.no_of_sides()

K = Quadrilateral()
K.no_of_sides()

R = Pentagon()
R.no_of_sides()

K = Hexagon()
K.no_of_sides()
