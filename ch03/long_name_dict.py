class LongNameDict(dict):
	"""Demonstration of extending the dict built-in."""
	def longest_key(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
		return longest

def main():
	longkeys = LongNameDict()
	longkeys['hello'] = 1
	longkeys['longest yet'] = 5
	longkeys['hello2'] = 'world'
	print(longkeys.longest_key())

if __name__ == '__main__':
	main()