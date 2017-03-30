import math

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

class MaxBinHeap:
	def __init__(self):
		# Python lists are implemented as arrays.
		self.heapList = []
		self.currentSize = 0

	def getSize(self):
		return self.currentSize

	def getHeapList(self):
		return self.heapList

	def parent(self, i):
		return (i-1)//2

	def left(self, i):
		return 2*i+1

	def right(self, i):
		return 2*i+2

	def minChild(self, i):
		if self.right(i) > self.currentSize-1:
			return self.left(i)
		else:
			if self.heapList[self.left(i)] <= self.heapList[self.right(i)]:
				return self.left(i)
			else:
				return self.right(i)

	def maxChild(self, i):
		if self.right(i) > self.currentSize-1:
			return self.left(i)
		else:
			if self.heapList[self.left(i)] > self.heapList[self.right(i)]:
				return self.left(i)
			else:
				return self.right(i)

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		if self.currentSize > 1:
			self.percUp(self.currentSize)

	def extract(self):
		if self.currentSize == 0:
			raise ValueError("Nothing to extract")
		else:
			temp = self.heapList[0]
			self.heapList[0] = self.heapList[self.currentSize-1]
			self.currentSize = self.currentSize - 1
			self.heapList.pop()
			self.percDown(0)
			return temp

	def find(self):
		return self.heapList[0]

	def copy(self, BinHeap):
		BinHeap.heapList = self.heapList

	def percUp(self, i):
		self.current = i-1
		while self.parent(self.current) >= 0:
			if self.heapList[self.current] > self.heapList[self.parent(self.current)]:
				tmp = self.heapList[self.parent(self.current)]
				self.heapList[self.parent(self.current)] = self.heapList[self.current]
				self.heapList[self.current] = tmp
			self.current = self.parent(self.current)

	def percDown(self, i):
		while 2*i+1 <= self.currentSize-1:
			mc = self.maxChild(i)
			if self.heapList[i] < self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def print(self):
		print(self.heapList)

	def BFS(self, element):
		for i in range(0, self.currentSize):
			if i == 0 and self.heapList[i] == element:
				print("Element", element, "found at depth the root")
			elif self.heapList[i] == element:
				print("Element", element, "found at depth", math.floor(math.log(i+1, 2)))
			# If you to return the nodes in tree, simply comment out the code above until
			# for-loop and remove the comment mark on the line below.
			# print(self.heapList[i], end=' ')

	def DFS(self):
		s = Stack()
		temp = MaxBinHeap()
		self.copy(temp)
		i = 0
		s.push(self.heapList[i])
		# self.DFShelper(s, i)
		# s.print()
		while (not s.isEmpty()):
			node = s.pop()
			print(node)
			if self.right(i) <= self.currentSize:
				i = self.right(i)
			s.push(self.heapList[i])
			# if self.right(i) <= self.currentSize:
			# 	s.push(self.heapList[self.right(i)])
			# if self.left(i) <= self.currentSize:
			# 	s.push(self.heapList[self.left(j)])
			# i = self.left(i)

	def DFShelper(self, stack, i):
		if i <= self.currentSize and self.left(i) <= self.currentSize:
			stack.push(self.heapList[self.left(i)])
			
			if self.left(i)+1 <= self.currentSize:
				stack.push(self.heapList[self.right(i)])
				# self.DFShelper(stack, self.right(i))
			self.DFShelper(stack, self.left(i))
		if i <= self.currentSize and self.right(i) <= self.currentSize:
			stack.push(self.heapList[self.right(i)])
			self.DFShelper(stack, self.right(i))




bh = MaxBinHeap()
# bh = MinBinHeap()
bh.insert(33)
bh.print()
bh.insert(17)
bh.print()
bh.insert(27)
bh.print()
bh.insert(14)
bh.print()
bh.insert(11)
bh.print()
bh.insert(18)
bh.print()
bh.insert(19)
bh.print()
bh.insert(21)
bh.print()
bh.insert(9)
bh.print()
bh.insert(8)
bh.print()
bh.insert(7)
bh.print()
bh.insert(6)
bh.print()
bh.insert(5)
bh.print()
bh.insert(4)
bh.print()
bh.insert(3)
bh.print()
bh.insert(2)
bh.print()
bh.insert(1)
bh.print()

bh.BFS(5)
bh.BFS(9)
bh.BFS(21)
bh.BFS(33)
bh.BFS(14)
bh.BFS(17)
bh.BFS(11)
bh.BFS(18)
bh.BFS(19)
bh.BFS(27)
bh.BFS(8)
bh.BFS(7)
bh.BFS(6)
bh.BFS(4)
bh.BFS(3)
bh.BFS(2)
bh.BFS(1)

bh2 = MaxBinHeap()
bh.copy(bh2)
# bh2.print()

bh.DFS()