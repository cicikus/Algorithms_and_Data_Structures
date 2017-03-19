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

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None

	def enqueue(self, data):
		if self.front == None:
			self.front = Node(data)
			self.rear = self.front
			print("self.rear=", self.rear.get_data(), " and self.front=",
				self.front.get_data(), sep='')
		else:
			new_node = Node(data)
			new_node.set_prev(self.rear)
			self.rear.set_next(new_node)
			self.rear = new_node
			print("self.rear=", self.rear.get_data(), " and self.front=",
				self.front.get_data(), sep='')

	def dequeue(self):
		if self.front == None:
			raise ValueError("Nothing to dequeue.")
		else:
			if self.front.get_next() == None:
				self.front = None
				self.rear = None
			else:
				self.front = self.front.get_next()
				self.front.set_prev(None)
		print("self.rear=", self.rear.get_data(), " and self.front=",
				self.front.get_data(), sep='')
		

	def print(self):
		current = self.rear
		while current:
			print(current.get_data(), end=' ')
			current = current.get_prev()
		print()


q1 = Queue()
q1.enqueue(5)
q1.enqueue(2)
q1.enqueue(7)
q1.enqueue(6)
q1.enqueue(3)
q1.print()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print()
q1.print()