class Node:

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class SinglyLinkedList:

	def __init__(self, head=None):
		self.head = head
		
	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
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

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def print(self):
		current = self.head
		while current:
			print(current.get_data())
			current = current.get_next()

	def reverse(self):
		current = self.head
		p = None
		n = Node()
		while current:
			n = current.get_next()
			current.set_next(p)
			p = current
			current = n
		self.head = p

	def concat(self, other):
		elem = other.head
		while elem:
			new_node = Node(elem.get_data())
			new_node.set_next(self.head)
			self.head = new_node
			elem = elem.get_next()


sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.print()
sll.reverse()
print()
sll.print()
sll.reverse()
print()
# sll.print()
# print()

sll2 = SinglyLinkedList()
sll2.insert(6)
sll2.insert(7)
sll2.insert(8)
sll2.insert(9)
sll2.insert(10)

sll.concat(sll2)
sll.print()
print()

sll2.print()