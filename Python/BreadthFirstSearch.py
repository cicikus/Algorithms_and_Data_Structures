class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def parent(self, i):
		return i // 2

	def left(self, i):
		return 2*i

	def right(self, i):
		return 2*i + 1

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percUp(self, i):
		while self.parent(i) > 0:
			if self.heapList[i] < self.heapList[self.parent(i)]:
				tmp = self.heapList[self.parent(i)]
				self.heapList[self.parent(i)] = self.heapList[i]
				self.heapList[i] = tmp
			i = self.parent(i)

bh = BinHeap()
bh.insert(33)
bh.insert(17)
bh.insert(27)
bh.insert(14)
bh.insert(11)
bh.insert(18)
bh.insert(19)
bh.insert(21)
bh.insert(9)
bh.insert(5)
print(bh.heapList)

