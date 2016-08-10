# Demonstration of using properties to return calculated values.

class AverageList(list):
	"""AverageList provides the ability to calculate the average of numbers."""

	@property
	def average(self):
		return sum(self) / len(self)


# Demonstration of class API
def main():
	a = AverageList([1, 2, 3, 4])
	print("Average = %f" % a.average)


# Import guard
if __name__ == '__main__':
	main()	
