from enum import Enum 
import queue

class Color(Enum):
	WHITE = 1
	GREY = 2
	BLACK = 3

class Vertex:

	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def initBFS(self):
		self.color = Color.WHITE
		self.distance = None
		self.parent = None

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def removeNeighbor(self, nbr):
		if nbr in self.connectedTo:
			del(self.connectedTo[nbr])
		

class Graph:

	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		self.numVertices = self.numVertices + 1
		return newVertex

	def removeVertex(self, key):
		if key in self.vertList:
			for v in self:
				if self.vertList[key] in v.connectedTo:
					v.removeNeighbor(self.vertList[key])
			del(self.vertList[key])

	def addEdge(self, f, t, weight=0):
		if f not in self.vertList:
			self.addVertex(f)
		if t not in self.vertList:
			self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], weight)

	def removeEdge(self, f, t):
		if f in self.vertList and t in self.vertList:
			self.vertList[f].removeNeighbor(self.vertList[t])

	def __contains__(self, key):
		return key in self.vertList

	def __iter__(self):
		return iter(self.vertList.values())

	def bfs(self, source):
		for v in self:
			v.initBFS()
		q = queue.Queue()

		self.vertList[source].color = Color.GREY
		self.vertList[source].distance = 0
		q.enqueue(self.vertList[source])

		while not q.isEmpty():
			vertex = q.dequeue()
			for nbr in vertex.connectedTo:
				if nbr.color == Color.WHITE:
					nbr.color = Color.GREY
					nbr.distance = vertex.distance + 1
					nbr.parent = vertex
					q.enqueue(nbr)
			vertex.color = Color.BLACK

	def printPath(self, dest):
		vertex = self.vertList[dest]
		if vertex.parent != None:
			self.printPath(vertex.parent.id)
		print(dest)

if __name__ == "__main__":
	graph = Graph()
	graph.addVertex("V0")
	graph.addVertex("V1")
	graph.addVertex("V2")
	graph.addVertex("V3")
	graph.addVertex("V4")
	graph.addVertex("V5")

	graph.addEdge("V0", "V1", 5)
	graph.addEdge("V0", "V3", 2)
	graph.addEdge("V45", "V100", 5)

	graph.removeVertex("V3")

	for v in graph:
		print(v)





