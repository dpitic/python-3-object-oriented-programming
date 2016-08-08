import math

# Demonstration of using built-in types.
# This module defines a square, represented by the coordinates of its vertices
# as a list of tuples. It defines a function to calculate the distance between
# two points and a function to calculate the perimeter of a polygon, defined
# by the coordinates of its vertices.

square = [(1,1), (1,2), (2,2), (2,1)]

def distance(p1, p2):
	"""Calculate the distance between two points."""
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def perimeter(polygon):
	"""Calculate the perimeter of a polygon defined by points."""
	perimeter = 0
	points = polygon + [polygon[0]]
	for i in range(len(polygon)):
		perimeter += distance(points[i], points[i+1])
	return perimeter


# Demonstration code
def main():
	print("Perimeter: %f" % perimeter(square))


# Import guard
if __name__ == '__main__':
	main()
