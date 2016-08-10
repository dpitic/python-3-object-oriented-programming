# Silly example demonstrating the concept of properties in Python. The class
# simply states whenever any of the methods are called.

class Silly:
	"""Silly class that states whenever any of the methods are called."""
	def _get_silly(self):
		print("You are getting silly")
		return self._silly

	def _set_silly(self, value):
		print("You are making silly {}".format(value))
		self._silly = value

	def _del_silly(self):
		print("Whoah, you killed silly!")
		del self._silly

	silly = property(_get_silly, _set_silly, _del_silly,
					"This is a silly property")


# Demonstration of class API
def main():
	s = Silly()
	s.silly = "funny"
	print("Getter: %s" % s.silly)
	del s.silly


# Import guard
if __name__ == '__main__':
	main()
