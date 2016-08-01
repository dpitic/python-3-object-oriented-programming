class ContactList(list):
	"""Demonstration of subclassing a built-in type."""
	def search(self, name):
		'''Return all contacts that contain the search value in their name.'''
		matching_contacts = []
		for contact in self:
			if name in contact.name:
				matching_contacts.append(contact)
		return matching_contacts

class Contact:
	"""Alternative implementation of Contact class using ContactList."""
	all_contacts = ContactList()

	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.all_contacts.append(self)

class Friend(Contact):
	"""
	Demonstration of overriding and use of super(). Friend is a Contact with
	a phone number.
	"""
	def __init__(self, name, email, phone):
		super().__init__(name, email)
		self.phone = phone
		

def main():
	c1 = Contact("John A", "johna@example.net")
	c2 = Contact("John B", "johnb@example.net")
	c3 = Contact("Jenna C", "jennac@example.net")
	# Access class variable through class
	print([c.name for c in Contact.all_contacts.search('John')])
	c4 = Friend("Friend D", "friendd@example.net", "555-5555")
	# Access class variable though instance
	print([c.name for c in c4.all_contacts.search('Friend')])

if __name__ == '__main__':
	main()
		
		