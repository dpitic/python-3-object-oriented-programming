class Contact:
	"""
	Contact class is responsible for maintaining a list of contacts. This is
	an example of class inheritance.
	"""
	all_contacts = []

	# Demonstrating the proper way to implement multiple inheritance. The base
	# class parameter list has to accept keyword arguments for any parameters
	# that are not required by every subclass implementation. The method must
	# freely accept unexpected arguments and pass them onto its super() call
	# in case they are necessary to later methods in the inheritance hierarchy.
	# The **kwargs parameter captures any additional parameters that a
	# particular method doesn't know how to handle and passes it up to the
	# next class with the super() call.
	def __init__(self, name='', email='', **kwargs):
		super().__init__(**kwargs)
		self.name = name
		self.email = email
		Contact.all_contacts.append(self)

class AddressHolder:
	"""Class used to hold addresses. Demonstration of multiple inheritance."""
	def __init__(self, street='', city='', state='', code='', **kwargs):
		super().__init__(**kwargs)
		self.street = street
		self.city = city
		self.state = state
		self.code = code

class Friend(Contact, AddressHolder):
	"""A friend is a contact with a phone number and an address."""
	def __init__(self, phone='', **kwargs):
		super().__init__(**kwargs)
		self.phone = phone

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
