class Inventory(object):
	"""
	Inventory class used to manage inventory items. This is an example of using
	exceptions to handle situatons which are not "exceptional circumstances".
	Specifically, when an item is out of stock, which is a perfectly normal 
	situation for an inventory application.

	In contrast, the same logic could have been coded using if...else, but this
	"""
	
	def lock(self, item_type):
		'''
		Select the type of item that is going to be manipulated. This method
		will lock the item so nobody else can manipulate the inventory until
		it's returned. This prevents selling the same item to two different
		customers.
		'''
		pass

	def unlock(self, item_type):
		'''Release the given type so that other customers can access it.'''
		pass

	def purchase(self, item_type):
		'''
		If the item is not locked, raise an exception. If the item_type does not
		exist, raise an exception. If the item is currently out of stock, raise
		an exception. If the item is available, subtract one item and return the
		number of items left.
		'''
		pass


# Demonstration code. Class implementatin is not complete!
def main():
	item_type = 'widget'
	inv = Inventory()
	inv.lock(item_type)
	try:
		num_left = inv.purchase(item_type)
	except InvalidItemTyp:
		print("Sorry, we don't sell {}".format(item_type))
	except OutOfStock:
		print("Sorry, that item is out of stock.")
	else:
		print("Purchase complete. There are {} {}s left"
			.format(num_left, item_type))
	finally:
		inv.unlock(item_type)


if __name__ == '__main__':
	main()