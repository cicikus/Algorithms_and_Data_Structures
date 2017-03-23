class Stack:
	def __init__(self):
		# Python 'lists' are implemented as arrays.
		# Therefore all operations will take constant time.
		# Also, the double underscore makes the variable private.
		self.__items = []

	def isEmpty(self):
		return self.__items == []

	def push(self, item):
		return self.__items.append(item)

	def pop(self):
		return self.__items.pop()

	def top(self):
		return self.__items[self.size() - 1]

	def size(self):
		return len(self.__items)

	def isEmpty(self):
		if self.size() == 0:
			return True
		else:
			return False

	def popAll(self):
		print(self.__items)
		del self.__items[:]

	def print(self):
		print(self.__items)


stack1 = Stack()
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(2)
stack1.push(1)
stack1.push(3)
print(stack1.top())
stack1.print()
stack1.pop()
stack1.print()
stack1.popAll()
stack1.print()