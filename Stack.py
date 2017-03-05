class Stack:
	def __init__(self):
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
		size = 0
		for x in self.items:
			size += 1
		return size

	def isEmpty(self):
		if self.size() == 0:
			return True
		else:
			return False

stack1 = Stack()
stack1.push('j')
stack1.push('a')
stack1.push('c')
stack1.push('o')
stack1.push('b')
stack1.push('s')
print(stack1.peek())