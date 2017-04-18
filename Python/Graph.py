class Graph:
	def __init__(self):
		self.nodeList = {}
		self.weights = {}
		self.numVertices = 0

	def addNode(self, node):
		self.nodeList[node] = []

	def addEdge(self, source, destination, weight):
		if source not in self.nodeList:
			raise KeyError("No such node exist.")
		isDestination = False
		for val in self.nodeList:
			if val == destination:
				isDestination = True
		if isDestination:
			self.nodeList[source].append(destination)
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

print(g.nodeList)
print(g.weights)

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