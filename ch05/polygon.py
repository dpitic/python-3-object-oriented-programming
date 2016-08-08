import math

# Implementation of the polygon perimeter example using OOP

class Point:
	"""Point class representing a point in 2D space."""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, p2):
		"""Calculate the distance between this point and the given point."""
		return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)


class Polygon:
	"""Polygon defined as a list of points."""
	def __init__(self, points=None):
		points = points if points else []
		self.vertices = []
		# Iterate through the list of tuples and convert them into Points. If
		# the object is not a tuple, assume it is a Point and add it to the
		# list of vertices for this polygon.
		for point in points:
			if isinstance(point, tuple):
				point = Point(*point)
			self.vertices.append(point)

	def add_point(self, point):
		"""Add a point to the polygon."""
		self.vertices.append(point)

	def perimeter(self):
		"""Calculate the perimeter of this polygon."""
		perimeter = 0
		points = self.vertices + [self.vertices[0]]
		for i in range(len(self.vertices)):
			perimeter += points[i].distance(points[i+1])
		return perimeter


# Demonstration code
def main():
	square_tuples = [(1,1), (1,2), (2,2), (2,1)]
	square = Polygon()
	for point in square_tuples:
#		square.add_point(Point(point[0], point[1]))
		square.add_point(Point(*point))
	print("Perimeter: %f" % square.perimeter())

	# Define another square using the list of tuples
	square2 = Polygon(square_tuples)
	print("Perimeter: %f" % square2.perimeter())


# Import guard
if __name__ == '__main__':
	main()
