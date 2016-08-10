# Implementation of the Silly class demonstrating the use of property
# decorators.

class Silly:
	"""
	Silly class that states whenever any of its methods are called, implemented
	using property decorators.
	"""

	@property
	def silly(self):
		"""This is a silly property"""
		print("You are getting silly")
		return self._silly

	@silly.setter
	def silly(self, value):
		print("You are making silly {}".format(value))
		self._silly = value

	@silly.deleter
	def silly(self):
		print("Whoah, you killed silly!")
		del self._silly


# Demonstration of class API
def main():
	s = Silly()
	s.silly = "funny"
	print("Getter: %s" % s.silly)
	del s.silly


# Import guard
if __name__ == '__main__':
	main()	
		