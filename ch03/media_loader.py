import abc

class MediaLoader(metaclass=abc.ABCMeta):
	"""
	Demonstration of creating an abstract base class (ABC). It documents the
	API that subclasses must provide.
	"""
	@abc.abstractmethod
	def play(self):
		pass

	@abc.abstractproperty
	def ext(self):
		pass

	@classmethod
	def __subclasshook__(cls, C):
		"""
		Allows any class that provides concrete implementations of all the
		abstract attributes of this abstract class to be considered a subclass
		of MediaLoader, even if it doesn't actually inherit from this class.
		"""
		if cls is MediaLoader:
			attrs = set(dir(C))
			if set(cls.__abstractmethods__) <= attrs:
				return True
		return NotImplemented

class Wav(MediaLoader):
	"""
	Class fails to implement the abstract attribute and abstract method. It is
	not possible to instantiate an object of this subclass. It is still a legal
	abstract class though.
	"""
	pass

class Ogg(MediaLoader):
	"""Subclass implements the abstract attributes which makes it possible to
	instantiate an object of this subclass.
	"""
	ext = ".ogg"
	def play(self):
		pass

# Demonstration code
def main():
	o = Ogg()		# Possible to instantiate a the subclass object
	x = Wav()		# Not possible to instantiate the subclass object.

# Import guard
if __name__ == '__main__':
	main()