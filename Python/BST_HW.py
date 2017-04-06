class TreeNode(object):
	def __init__(self, data, left=None, right=None, parent=None):
		self.data = data
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self, key, lc, rc):
		self.key = key
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self


class BinarySearchTree(TreeNode):

	def __init__(self, newroot, rc=None, lc=None, parent=None):
		super().__init__(newroot)
		self.leftChild = None
		self.rightChild = None
		self.parent = None
		self.size = 0

	def insert(self, data):
		newnode = BinarySearchTree(data)

		if self.data > newnode.data:
			if self.leftChild is None:
				self.leftChild = newnode
				self.leftChild.parent = self
			else:
				self.leftChild.insert(newnode.data)
		else:
			if self.rightChild is None:
				self.rightChild = newnode
				self.rightChild.parent = self
			else:
				self.rightChild.insert(newnode.data)

	def DFS(self):
		current = self 
		s = []
		done = 0
		while(not done):
			if current is not None:
				s.append(current)
				current = current.leftChild 
			else:
				if(len(s)>0):
					current = s.pop()
					print(current.data)
					current = current.rightChild 
				else:
					done = 1

	def __iter__(self):
		self.current = self
		self.s = []
		self.done = 0
		return self

	def __next__(self):
		if self.done = 1:
			raise StopIteration
		if self.current is not None:
			self.s.append(self.current)
			self.current = self.current.leftChild
		else:
			if(len(self.s)>0):
					self.current = self.s.pop()
					self.current = current.rightChild 
				else:
					self.done = 1

	def nextHelper(self):
		current = self 
		self.iterHelp = []
		s = []
		done = 0
		while(not done):
			if current is not None:
				s.append(current)
				current = current.leftChild 
			else:
				if(len(s)>0):
					current = s.pop()
					self.iterHelp.append(current)
					current = current.rightChild 
				else:
					done = 1


mytree = BinarySearchTree(8)
mytree.insert(3)
mytree.insert(10)

print("Root:", mytree.data)
print("Root's left child:", mytree.leftChild.data)
print("Root's right child:", mytree.rightChild.data)

mytree.insert(1)

# print(mytree.leftChild.leftChild.data)

mytree.insert(6)
mytree.insert(4)
mytree.insert(7)
mytree.insert(14)
mytree.insert(13)

print("Printing via depth-first traversal")
mytree.DFS()
print()

print("Printing with iterator")
for node in mytree:
	print(node.data)

print()

print("Printing with iterator")
for node in mytree:
	print(node.data)

print()

print("Printing with iterator")
for node in mytree:
	print(node.data)