class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def removeNeighbor(self, nbr):
    	del(self.connectedTo[nbr])

    def __str__(self):
    	return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def removeEdge(self, f, t):
    	if f in self.vertList and t in self.vertList:
    		self.vertList[f].removeNeighbor(self.vertList[t])

    def removeVertex(self, key):
    	for v in self.vertList:
    		vertex = self.vertList[v]
    		if self.vertList[key] in vertex.getConnections():
    			vertex.removeNeighbor(self.vertList[key])
    	del(self.vertList[key])

    def getVertices(self):
        return self.vertList.keys()


graph = Graph()
graph.addVertex("V0")
graph.addVertex("V1")
graph.addVertex("V2")
graph.addVertex("V3")
graph.addVertex("V4")
graph.addVertex("V5")

graph.addEdge("V0", "V2", 5)
graph.addEdge("V0", "V8", 5)

# graph.removeEdge("V17", "V2")
graph.removeVertex("V8")

for x in graph:
	print(x)

