# Implementation of the Color class to demonstrate the use of properties. These
# make methods look like attributes which enables client code to be written to
# use direct member access. This permits the implementation to change while
# maintaining the same interface.

class Color:
	"""
	Color class with implementation evolved from not using private attributes
	and accessor methods to using properties. Only the name attribute is
	transitioned to a property. The interface remains the same as it it were
	a public attribute, enabling reading and writing using direct access.
	"""

	def __init__(self, rgb_value, name):
		self.rgb_value = rgb_value
		self._name = name 			# changed to private

	# Private setter for name implementing some validation
	def _set_name(self, name):
		if not name:
			raise Exception("Invalid name")
		self._name = name

	# Private getter for name
	def _get_name(self):
		return self._name

	# The property keyword makes methods look like attributes, enabling direct
	# access, with custom implementation
	name = property(_get_name, _set_name)


# Demonstration API
def main():
	c = Color("#0000ff", "bright red")
	print("Name: %s" % c.name)
	c.name = "red"
	print("Name: %s" % c.name)
	# Expect an exception here; demonstrating custom setter validation
	c.name = ""


# Import guard
if __name__ == '__main__':
	main()
