class Stack:
	def __init__(self):
		# Python 'lists' are implemented as arrays.
		# Therefore all operations will take constant time.
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[self.size() - 1]

	def size(self):
		return len(self.items)

	def isEmpty(self):
		if self.size() == 0:
			return True
		else:
			return False

	def popAll(self):
		print(self.items)
		del self.items[:]

	def print(self):
		print(self.items)


stack1 = Stack()
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(2)
stack1.push(1)
stack1.push(3)
print(stack1.peek())
stack1.print()
stack1.popAll()
stack1.print()