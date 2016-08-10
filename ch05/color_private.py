# This class is an example of implementing private attributes and providing
# a public interface to access them. This is typical in Java, but it's not
# the preferred style in Python.

class Color:
	"""
	Implementation of a colour class with a property interface style common
	in Java.
	"""
	def __init__(self, rgb_value, name):
		self._rgb_value = rgb_value
		self._name = name

	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name


# Demonstration of class API
def main():
	c = Color("#ff0000", "bright red")
	print("Name: %s" % c.get_name())
	c.set_name("red")
	print("Name: %s" % c.get_name())


# Import guard
if __name__ == '__main__':
	main()
