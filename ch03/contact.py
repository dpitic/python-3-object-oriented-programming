class Contact:
	"""
	Contact class is responsible for maintaining a list of contacts. This is
	an example of class inheritance.
	"""
	all_contacts = []

	def __init__(self, name, email):
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)

class Supplier(Contact):
	"""Suppliers are contacts who can provide orders of supplies."""
	def order(self, order):
		print("If this were a real system we would send "
			"'{}' order to '{}'".format(order, self.name))

def main():
	c = Contact("Some Body", "somebody@example.net")
	s = Supplier("Sup Plier", "supplier@example.net")
	print(c.name, c.email, s.name, s.email)
	print(c.all_contacts)
	s.order("I need pliers")
	# Contact does not have an order() method; expect an exception here
	c.order("I need an exception")

if __name__ == '__main__':
	main()
		