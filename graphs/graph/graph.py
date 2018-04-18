class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self,nbr,weight = 0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connected])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]
		
a = Vertex('V0')
b = Vertex('V1')
c = Vertex('V2')

a.addNeighbor(b)
a.addNeighbor(c)

print(a)
print([x.id for x in a.getConnections()])
