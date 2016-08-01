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

def main():
	c1 = Contact("John A", "johna@example.net")
	c2 = Contact("John B", "johnb@example.net")
	c3 = Contact("Jenna C", "jennac@example.net")
	print([c.name for c in Contact.all_contacts.search('John')])

if __name__ == '__main__':
	main()
		
		