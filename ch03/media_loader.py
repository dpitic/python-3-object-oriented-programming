# Abstract Base Class module
import abc

# Metaclass is used in Python for metaclass programming. The ABCMeta metaclass
# gives this class superclass abilities.
class MediaLoader(metaclass=abc.ABCMeta):
	"""
	Demonstration of creating an abstract base class (ABC). It documents the
	API that subclasses must provide.
	"""

	# Decorating this method as an abstract method which subclasses must
	# implement in order to be concrete classes.
	@abc.abstractmethod
	def play(self):
		pass

	# Decorating this property as an abstract property which subclasses must
	# implement in order to be concrete classes.
	@abc.abstractproperty
	def ext(self):
		pass

	# Decorator to mark the method as a class method so that it can be called
	# on a class instead of an instantiated object.
	@classmethod
	def __subclasshook__(cls, C):
		"""
		Allows any class that provides concrete implementations of all the
		abstract attributes of this abstract class to be considered a subclass
		of MediaLoader, even if it doesn't actually inherit from this class. Its
		purpose is to answer the question:
			Is the class C a subclass of this class?
		"""
		if cls is MediaLoader:		# Check if method was called on this class
			# Get the set of methods and properties the class has, including
			# any parent classes in its class hierarchy.
			attrs = set(dir(C))
			# Check whether the set of abstract methods in this class have
			# been supplied in the candidate class (doesn't check 
			# implementation)
			if set(cls.__abstractmethods__) <= attrs:
				return True		# Subclass supplying set of abstract methods
		return NotImplemented	# Not a subclass or not all abstract methods
								# implemented.

class Wav(MediaLoader):
	"""
	Class fails to implement the abstract attribute and abstract method. It is
	not possible to instantiate an object of this subclass. It is still a legal
	abstract class though.
	"""
	pass

class OggExplicitSubClass(MediaLoader):
	"""
	Subclass implements the abstract attributes which makes it possible to
	instantiate an object of this subclass. This subclass explicitly extends
	the abstract base class MediaLoader.
	"""
	ext = ".ogg"
	def play(self):
		print("Playing an ogg file with an explicitly defined MediaLoader"
			" subclass.")

class OggNotExplicitSubClass:
	"""
	Definition of the Ogg class as a subclass of MediaLoader, without explicitly
	extending the MediaLoader class. Example of using duck typing instead of
	inheritance.
	"""
	ext = ".ogg"
	def play(self):
		print("Playing an ogg file with a MediaLoader subclass that doesn't"
			" explicitly extend MediaLoader.")

# Demonstration code
def main():
	o = OggExplicitSubClass()	# Possible to instantiate a the subclass object
	print("Is OggExplicitSubClass a subclass of MediaLoader? {}".format(repr(
		issubclass(OggExplicitSubClass, MediaLoader))))
	print("Is o an instance of MediaLoader? {}".format(repr(
		isinstance(o, MediaLoader))))

	# Possible to instantiate a subclass object with a duck type class
	onesc = OggNotExplicitSubClass()
	print("Is OggNotExplicitSubclass a subclass of MediaLoader? {}".
		format(repr(issubclass(OggNotExplicitSubClass, MediaLoader))))
	print("Is onesc an instance of MediaLoader? {}".format(repr(
		isinstance(onesc, MediaLoader))))
	# Expect an exception after the next statement
	x = Wav()				# Not possible to instantiate the subclass object.

# Import guard
if __name__ == '__main__':
	main()