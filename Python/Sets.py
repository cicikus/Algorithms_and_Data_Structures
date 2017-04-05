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

class ListSet:

	def __init__(self, head=None):
		self.__head = head
		self.current = Node()
		self.current.set_next(self.__head)

	def getHead(self):
		return self.__head

	def insert(self, data):
		if self.__head is None:
			new_node = Node(data)
			new_node.set_next(self.__head)
			self.__head = new_node
			self.current.set_next(self.__head)
		else:
			new_node = Node(data)
			current = self.__head
			while current and current.get_next():
				current = current.get_next()
			current.set_next(new_node)

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

	def __iter__(self):
		# self.current = Node()
		# self.current.set_next(self.__head)
		return self

	def __next__(self):
		if self.current.get_next() == None:
			self.current = Node()
			self.current.set_next(self.__head)
			# Debug code:
			# print("self.current.get_next().get_data() =", self.current.get_next().get_data())
			# print(self.current.get_data())
			raise StopIteration
		self.current = self.current.get_next()
		return self.current


ls = ListSet()
ls.insert(1)
ls.insert(2)
ls.insert(3)
ls.insert(4)
ls.insert(5)
print("ls: ")
ls.print()

ls.insert(20)
ls.print()
ls.insert(21)
ls.print()
ls.insert(22)
ls.print()
print("ls.current", ls.current.get_data())

# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()
# ls.__next__()

for node in ls:
	print(node.get_data(), end=' ')
print()

for node in ls:
	print(node.get_data(), end=' ')
print()
