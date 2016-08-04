from collections import Container

class OddContainer:
	"""
	Container used for storing odd integers. This is to demonstrate that even
	though OddContainer did not subclass Container, Python still considers that
	OddContainer is-a Container. This has the advantage of creating is-a
	relationships without the coupling resulting from inheritance.

	Any class that has the __contains__() method is-a Container and can be
	queried by the "in" keyword ("in" delegates to __contains__()).
	"""
	def __contains__(self, x):
		if not isinstance(x, int) or not x % 2:
			return False
		return True

# Sample code to prove that OddContainer is-a Container
def main():
	odd_container = OddContainer()
	# Check instance and subclass
	print(isinstance(odd_container, Container))
	print(issubclass(OddContainer, Container))
	# Use of "in"
	print("1 in odd_container {}".format(repr(1 in odd_container)))
	print("2 in odd_container {}".format(repr(2 in odd_container)))
	print("3 in odd_container {}".format(repr(3 in odd_container)))


if __name__ == '__main__':
	main()