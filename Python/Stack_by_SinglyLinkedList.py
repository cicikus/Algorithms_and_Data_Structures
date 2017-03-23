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

class Stack:
	def __init__(self, head=None):
		self.head = head
		
	def top(self):
		return self.head

	def push(self, data):
		# Prepends elements
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		
	def pop(self):
		if self.head == None:
			raise ValueError("Nothing to pop.")
		else:
			print("Popping ", self.head.get_data())
			self.head = self.head.get_next()

	def print(self):
		current = self.head
		while current != None:
			print(current.get_data(), end=' ')
			current = current.get_next()
		print()

s = Stack()
s.push(5)
s.push(9)
s.push(8)
s.push(1)
s.push(3)
s.push(4)
s.print()
s.pop()
s.print()
while s.top() != None:
	s.pop()
	s.print()
	