class SecretString(object):
	'''
	A not-at-all secure way to store a secret string. This is a demonstration of
	name mangling in Python.
	'''
	def __init__(self, plain_text, pass_phrase):
		# The instance variables should have their names mangled
		self.__plain_text = plain_text
		self.__pass_phrase = pass_phrase

	def decrypt(self, pass_phrase):
		'''Only show the plain text string if the pass phrase is correct.'''
		if pass_phrase == self.__pass_phrase:
			return self.__plain_text
		else:
			return ''

# Demonstration of class API usage
def main():
	secret_string = SecretString("ACME: Top Secret", "antwerp")
	# Incorrect pass phrase should produce an empty string
	print(secret_string.decrypt("incorrect_pass_phrase"))
	# Accessing the name mangled instance variable which is prefixed with
	# _<classname>
	print(secret_string._SecretString__plain_text)
	# Correct pass phrase should produce the plain text string
	print(secret_string.decrypt("antwerp"))
	# The __plain_text instance variable is name mangled so it should not
	# be accessible by name. Expect an error to be thrown here.
	print(secret_string.__plain_text)

# Module guard to ensure the module can be imported without executing the code
# and to execute the API demonstration code when the module is explicitly run
if __name__ == '__main__':
	main()
		