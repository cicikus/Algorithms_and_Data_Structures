class RingBuffer:
	def __init__(self, n):
		self.n = n
		self.elements = [None for i in range(self.n)]
		self.size = 0
		self.begin = 0

	def overflow(self):
		return self.size == self.n

	def underflow(self):
		return self.size == 0

	def enqueue(self, x):
		if self.overflow():
			raise Exception("Buffer overflow")
		self.elements[(self.begin+self.size)%self.n] = x
		self.size += 1

	def dequeue(self):
		if self.underflow():
			raise Exception("Buffer underflow")
		self.temp = self.elements[self.begin]
		self.elements[(self.begin)] = None
		self.begin = (self.begin+1)%self.n
		self.size -= 1
		print("Dequeued", self.temp)

	def get(self):
		return self.elements

bufsize = 4
buf = RingBuffer(bufsize)
for i in range(bufsize):
	buf.enqueue(i)
	print(buf.get())
for i in range(bufsize):
	buf.dequeue()
	print(buf.get())

buf.enqueue(10)
print(buf.get())
buf.enqueue(11)
print(buf.get())
buf.dequeue()
print(buf.get())
buf.enqueue(12)
print(buf.get())
buf.enqueue(13)
print(buf.get())
buf.dequeue()
print(buf.get())
buf.enqueue(14)
print(buf.get())
buf.enqueue(15)
print(buf.get())
buf.enqueue(15)