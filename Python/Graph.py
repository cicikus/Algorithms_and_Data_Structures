class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def dequeueAt(self, index):
		return self.items.pop(index)

	def size(self):
		return len(self.items)

	def getItems(self):
		return self.items

class Graph:
	def __init__(self):
		self.nodeList = {}
		self.weights = {}
		self.numVertices = 0

	def addNode(self, node):
		self.nodeList[node] = set([])

	def addEdge(self, source, destination, weight):
		if source not in self.nodeList:
			raise KeyError("No such node exist.")
		isDestination = False
		for val in self.nodeList:
			if val == destination:
				isDestination = True
		if isDestination:
			# print("Debug start")
			# print(type(self.nodeList[source]))
			# print(type(set([destination])))
			# print(self.nodeList[source] | set([destination]))
			# print("Debug end")
			self.nodeList[source] = self.nodeList[source] | set([destination])
			self.nodeList[destination] = self.nodeList[destination] | set([source])
			self.weights[(source, destination)] = weight
		else:
			raise ValueError("No such destination for ", source)

	def incoming(self, vertex):
		incoming = []
		for i in self.nodeList:
			for j in self.nodeList[i]:
				if j == vertex:
					incoming.append(i)
		return incoming

	def outgoing(self, vertex):
		return self.nodeList[vertex]

	def getEdges(self, vertex):
		inc = self.incoming(vertex)
		out = self.outgoing(vertex)
		print("Incoming: ", inc)
		print("Outgoung: ", out)

	def getNodes(self):
		return self.nodeList.keys()

	def getNodeList(self):
		return self.nodeList


def bfs(graph, start):
	temp_graph = graph.getNodeList()
	working = Queue()
	working.enqueue(start)
	visited = []
	visited.append(start)
	while not working.isEmpty():
		vertex = working.dequeue()
		print(vertex)
		# print("visited: ", visited)
		# print("working: ", working.getItems())
		# counter = 0
		for i in temp_graph[vertex]:
			# if counter == 2:
			# 	print("visited: ", visited)
			# 	print("working: ", working.getItems())
			# 	break
			if not i in visited:
				working.enqueue(i)
				visited.append(i)
			# counter += 1

g = Graph()
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')
g.addNode('F')
print(g.getNodes())

print(g.incoming('A'))
print(g.outgoing('A'))

g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 2)
g.addEdge('A', 'F', 3)

# print(g.nodeList)
# print(g.weights)

print("A incoming:", g.incoming('A'))
print("A outgoing:", g.outgoing('A'))

g.addEdge('B', 'C', 4)
g.addEdge('B', 'D', 5)

g.addEdge('C', 'D', 6)

g.addEdge('D', 'C', 7)

g.addEdge('E', 'F', 8)

g.addEdge('F', 'A', 9)
g.addEdge('F', 'C', 10)

print("A incoming:", g.incoming('A'))
print("A outgoing:", g.outgoing('A'))

print("B incoming:", g.incoming('B'))
print("B outgoing:", g.outgoing('B'))

g.getEdges('B')
print("Nodes:", g.getNodes())
print(g.nodeList)
print(g.weights)

try:
	g.addEdge('A', 'G', 11)
except ValueError:
	print("Value Error")
except ValueError:
	print("Key Error")

try:
	g.addEdge('G', 'A', 12)
except ValueError:
	print("Value Error")
except KeyError:
	print("Key Error")

bfs(g, 'A')


g2 = Graph()
g2.addNode('A')
g2.addNode('B')
g2.addNode('C')
g2.addNode('D')
g2.addNode('E')
g2.addNode('F')
g2.addNode('G')
g2.addNode('H')
g2.addNode('S')

g2.addEdge('A', 'B', 0)
g2.addEdge('A', 'S', 0)
g2.addEdge('S', 'C', 0)
g2.addEdge('S', 'G', 0)
g2.addEdge('C', 'D', 0)
g2.addEdge('C', 'E', 0)
g2.addEdge('C', 'F', 0)
g2.addEdge('G', 'F', 0)
g2.addEdge('G', 'H', 0)
g2.addEdge('H', 'E', 0)
print(g2.getNodes())
print()
bfs(g2, 'A')
