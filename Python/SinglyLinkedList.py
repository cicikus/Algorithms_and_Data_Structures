class Node:

	def __init__(self, data=None, next_node=None):
		self.__data = data
		self.next_node = next_node

	def get_data(self):
		return self.__data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class SinglyLinkedList:

	def __init__(self, head=None):
		self.__head = head

	def getHead(self):
		return self.__head
		
	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.__head)
		self.__head = new_node

	def insertEnd(self, data):
		new_node = Node(data)
		current = self.__head
		while current and current.get_next():
			current = current.get_next()
		current.set_next(new_node)

	def size(self):
		current = self.__head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def search(self, data):
		current = self.__head
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
		current = self.__head
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
			self.__head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def print(self):
		current = self.__head
		while current:
			print(current.get_data(), end=' ')
			current = current.get_next()
		print()

	def reverse(self):
		current = self.__head
		p = None
		n = Node()
		while current:
			n = current.get_next()
			current.set_next(p)
			p = current
			current = n
		self.__head = p

	def concat(self, other):
		elem = other.getHead()
		while elem:
			new_node = Node(elem.get_data())
			new_node.set_next(self.__head)
			self.__head = new_node
			elem = elem.get_next()


sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
print("sll: ")
sll.print()
sll.reverse()
print("\nsll after reversed: ")
sll.print()
sll.reverse()
print("\nsll after reversed again: ")
sll.print()
print()

# sll2 = SinglyLinkedList()
# sll2.insert(6)
# sll2.insert(7)
# sll2.insert(8)
# sll2.insert(9)
# sll2.insert(10)
# print("sll2: ")
# sll2.print()
# print()

# sll.concat(sll2)
# print("sll after concatenated with sll2: ")
# sll.print()

# print()
# print()
# print(sll2.getHead().get_data())
# print(sll2.head.data)

sll.insertEnd(20)
sll.print()
sll.insertEnd(21)
sll.print()
sll.insertEnd(22)
sll.print()
