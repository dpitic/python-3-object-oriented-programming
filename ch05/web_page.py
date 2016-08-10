from urllib.request import urlopen
import time

# A more realistic example of the use of Python class properties. This example
# caches a value as a private attribute on the first retrieval, and then
# returns the cached value on subsequent requests.

class WebPage:
	"""WebPage serves web pages with content caching."""
	def __init__(self, url):
		self.url = url
		self._content = None

	@property
	def content(self):
		if not self._content:
			print("Retrieving New Page...")
			self._content = urlopen(self.url).read()
		return self._content


# Demonstration of class API
def main():
	webpage = WebPage("http://ccphillips.net/")
	now = time.time()
	content1 = webpage.content
	print("Time lapse: %f" % (time.time() - now))
	now = time.time()
	content2 = webpage.content
	print("Time lapse: %f" % (time.time() - now))
	print("Confirm content is identical %s" % (content2 == content1))


# Import guard
if __name__ == '__main__':
	main()
