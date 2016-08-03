class AudioFile:
	"""
	Demonstration of polymorphism where different behavours occur depending on
	which subclass is being used, without explicitly knowing what the subclass
	actually is.

	The AudioFile class represents a generic audio object that a media player
	would play. However, the details of playing different types of audio
	files depend on the specific type of audio file, which can be represented
	by different subclasses of AudioFile.
	"""
	def __init__(self, filename):
		# The superclass has access to the subclass instance variables. Ensure
		# the audio file being specified is the correct format based on the
		# file extension.
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")
		self.filename = filename

class MP3File(AudioFile):
	"""MP3 audio file"""
	ext = "mp3"

	def play(self):
		print("Playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
	"""Wav audio file"""
	ext = "wav"

	def play(self):
		print("Playing {} as wav".format(self.filename))

class OggFile(AudioFile):
	"""Ogg audio file"""
	ext = "ogg"

	def play(self):
		print("Playing {} an ogg".format(self.filename))

class FlacFile:
	"""
	Demonstration of duck typing where any object that provides the required
	behaviour can be used without it having to be a subclass.
	"""
	def __init__(self, filename):
		if not filename.endswith(".flac"):
			raise Exception("Invalid file format")
		self.filename = filename
	
	def play(self):
		print("Playing {} as flac".format(self.filename))

# Demonstrate the usage of the AudioFile API
def main():
	ogg = OggFile("myfile.ogg")
	ogg.play()
	mp3 = MP3File("myfile.mp3")
	mp3.play()
	# Demonstrate duck typing in Python. The next object is not a subclass
	# of AudioFile, but it has the same play() interface.
	flac = FlacFile("myfile.flac")
	flac.play()
	# Expect an exception here trying to define an mp3 audio file that is not
	# an mp3
	not_an_mp3 = MP3File("myfile.ogg")

# Module import guard
if __name__ == '__main__':
	main()