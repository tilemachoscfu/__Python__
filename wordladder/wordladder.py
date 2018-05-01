import graph

wordsGraph = graph.Graph()
wordsDict = {} 
wordsFile = open("words.txt", "r")

for line in wordsFile:
	word = line[:-1]
	wordsGraph.addVertex(word)

	for i in range(0,4):
		template = word[:i] + '_' + word[i+1:]
		
		if template in wordsDict:
			wordsDict[template].append(word)
		else:
			wordsDict[template] = [word]

for item in wordsDict:
	for w1 in wordsDict[item]:
		for w2 in wordsDict[item]:
			if w1 != w2:
				wordsGraph.addEdge(w1, w2)


wordsGraph.bfs("fail")
wordsGraph.printPath("pool")