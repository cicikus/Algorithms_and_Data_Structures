class Node:
	def __init__(self, data=None, next_node=None):
		self.__data = data
		self.__next_node = next_node

	def get_data(self):
		return self.__data

	def get_next(self):
		return self.__next_node

	def set_next(self, new_next):
		self.__next_node = new_next

class SinglyLinkedList:
	def __init__(self, head=None):
		self.__head = head
		
	def getHead(self):
		return self.__head

	def insert(self, data):
		# Prepends elements
		new_node = Node(data)
		new_node.set_next(self.__head)
		self.__head = new_node

	def insertEnd(self, data):
		# Appends elements
		if self.__head == None:
			self.insert(data)
		else:
			new_node = Node(data)
			current = self.__head
			while current.get_next() != None:
				current = current.get_next()
			current.set_next(new_node)

	def pop(self):
		if self.__head == None:
			raise ValueError("Nothing to pop.")
		else:
			self.__head = self.__head.get_next()

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

class Queue:
	def __init__(self):
		self.items = SinglyLinkedList()
		self.items_reversed = SinglyLinkedList()

	def isEmpty(self):
		return self.items.size() == 0

	def enqueue(self, data):
		self.items.insert(data)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return self.items.size()

	def dequeueAll(self):
		while self.items.size() != 0:
			print("Popping", self.items.getHead().get_data())
			self.items.pop()

	def print(self):
		self.items.print()


sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.print()
sll.pop()
sll.pop()
sll.print()
sll.pop()
sll.pop()
sll.print()
sll.pop()
sll.print()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Printing queue: ")
q.print()
q.dequeueAll()


sll.insertEnd(1)
sll.insertEnd(2)
sll.insertEnd(3)
sll.insertEnd(4)
sll.insertEnd(5)
print()
print("Printing Singly Linked List: ")
sll.print()
