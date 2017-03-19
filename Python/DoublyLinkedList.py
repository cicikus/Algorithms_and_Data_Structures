class Node:

	def __init__(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next_node = next_node
		self.prev_node = prev_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

	def get_prev(self):
		return self.prev_node

	def set_prev(self, new_prev):
		self.prev_node = new_prev

class DoublyLinkedList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail
		
	def insertBeginning(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			new_node.set_next(self.head)
			self.head.set_prev(new_node)
			self.tail = self.head
			self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		return current

	# def delete(self, data):
	# 	current = self.head
	# 	previous = None
	# 	found = False
	# 	while current and found is False:
	# 		if current.get_data() == data:
	# 			found = True
	# 		else:
	# 			previous = current
	# 			current = current.get_next()
	# 	if current is None:
	# 		raise ValueError("Data not in list")
	# 	if previous is None:
	# 		self.head = current.get_next()
	# 	else:
	# 		previous.set_next(current.get_next())

	def print(self):
		current = self.head
		while current:
			print(current.get_data())
			current = current.get_next()

	# def reverse(self):
	# 	current = self.head
	# 	p = None
	# 	n = Node()
	# 	while current:
	# 		n = current.get_next()
	# 		current.set_next(p)
	# 		p = current
	# 		current = n
	# 	self.head = p

	# def concat(self, other):
	# 	elem = other.head
	# 	while elem:
	# 		new_node = Node(elem.get_data())
	# 		new_node.set_next(self.head)
	# 		self.head = new_node
	# 		elem = elem.get_next()


dll = DoublyLinkedList()
dll.insertBeginning(1)
dll.insertBeginning(2)
dll.insertBeginning(3)
dll.insertBeginning(4)
dll.insertBeginning(5)
dll.print()
print()
