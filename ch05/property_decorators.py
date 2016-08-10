# Demonstration of using decorators to define properties. The property function
# can be used with the decorator syntax to turn a get method into a property.

class Foo:
	"""Foo class demonstrates the use of decorators to define properties."""

	# This defines a property using the getter method
	@property
	def foo(self):
		return self._foo
	
	# Using the same name for the getter and setter methods is not required.
	# Doing this helps group the multiple methods that access one property
	# together.
	@foo.setter
	def foo(self, value):
		self._foo = value
