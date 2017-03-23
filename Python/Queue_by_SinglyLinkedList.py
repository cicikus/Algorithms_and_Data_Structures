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

	def Empty(self):
		self.__head

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

	def copy(self, other):
		current = self.__head
		while current:
			other.insertEnd(current.get_data())
			current = current.get_next()

class Queue:
	def __init__(self):
		self.into = SinglyLinkedList()
		self.out = SinglyLinkedList()

	def enqueue(self, data):
		print("Inserted ", data)
		self.into.insert(data)

	def dequeue(self):
		if self.into.getHead() == None and self.out.getHead() == None:
			return None
		elif self.out.getHead() == None:
			temp_list = SinglyLinkedList()
			self.into.copy(temp_list)
			temp_list.reverse()
			temp_list.copy(self.out)
			# self.out.print()
		temp = self.out.getHead()
		self.out.pop()
		print("Popped ", temp.get_data())

	def print(self):
		if self.out.getHead() == None:
			print("In: ", end='')
			self.into.print()
		else:
			temp = SinglyLinkedList()
			self.out.copy(temp)
			temp.reverse()
			print("Out: ", end='')
			temp.print()
			print("In: ", end='')
			self.into.print()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Printing queue: ")
q.print()
q.dequeue()
print("Printing queue: ")
q.print()
q.dequeue()
print("Printing queue: ")
q.print()
q.dequeue()
print("Printing queue: ")
q.print()
q.enqueue(50)
print("Printing queue: ")
q.print()
q.enqueue(51)
print("Printing queue: ")
q.print()
q.enqueue(52)
print("Printing queue: ")
q.print()
q.enqueue(53)
print("Printing queue: ")
q.print()
# q.dequeueAll()