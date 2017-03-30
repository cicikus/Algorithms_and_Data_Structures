# class Node:
# 	def __init__(self, data=None):
# 		self.data = data 
# 		self.lchild = None
# 		self.rchild = None

# 	def getLeft(self):
# 		return self.lchild

# 	def getRight(self):
# 		return self.rchild

# 	def getData(self):
# 		return self.data

# 	def setLeft(self, newnode):
# 		self.lchild = newnode

# 	def setRight(self, newnode):
# 		self.rchild = newnode

# 	def setData(self, data):
# 		self.data = data

# class BinaryTree:
# 	def __init__(self, data=None):
# 		self.root = Node(data)
 
# 	def insertLeft(self, data):
# 		if self.root.getData() == None:
# 			print("1")
# 			newnode = Node(data)
# 			self.root = newnode
# 		else:
# 			print("2")
# 			current = self.root
# 			while current.getLeft() != None:
# 				current = current.getLeft()
# 			newnode = Node(data)
# 			current.setLeft(newnode)

# 	def insertRight(self, data):
# 		if self.root.getData() == None:
# 			print("1")
# 			newnode = Node(data)
# 			self.root = newnode
# 		else:
# 			print("2")
# 			current = self.root
# 			while current.getRight() != None:
# 				current = current.getRight()
# 			newnode = Node(data)
# 			current.setLeft(newnode)

# 	def getRoot(self):
# 		return self.root

# 	def setRoot(self, newnode):
# 		self.root = newnode

# 	def setRootVal(self, data):
# 		self.root.setData(data)

# 	def getRootVal(self):
# 		return self.root.getData()

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)



class BinaryTree:
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key


def DFS(BinTree):
	if BinTree == None:
		return
	else:
		DFS(BinTree.getLeftChild())
		DFS(BinTree.getRightChild())
		print(BinTree.getRootVal(), end=' ')


def BFS(BinTree):
	q = Queue()
	q.enqueue(BinTree.getRootVal())
	temp = BinTree
	print(temp.getRootVal())
	while temp != None:
		print(temp)
		q.enqueue(temp.getLeftChild())
		q.enqueue(temp.getRightChild())
		temp = q.dequeue()

class Node:
 
	# A utility function to create a new node
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None
 
 

def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)
 
def printGivenLevel(root , level):
	if root is None:
		return
	if level == 1:
		print "%d" %(root.data),
	elif level > 1 :
		printGivenLevel(root.left , level-1)
		printGivenLevel(root.right , level-1)
 

def height(BinTree):
	if BinTree is None:
		return 0
	else :
		lheight = height(BinTree.getLeftChild)
		rheight = height(BinTree.getRightChild)
 
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1


b = BinaryTree(1)
b.insertLeft(2)
b.insertRight(3)
b.insertLeft(4)
b.insertRight(5)
b.insertLeft(6)
b.insertRight(7)
b.insertLeft(8)
b.insertRight(9)


print("\nDFS:")
DFS(b)
print(' ')
print("\nBFS:")
BFS(b)
print()