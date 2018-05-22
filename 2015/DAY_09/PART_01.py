import sys
from queue import Queue
from copy import deepcopy

class Path:
	def __init__(self, start):
		self.visited = set()
		self.visited.add(start)
		self.curr = start
		self.distance = 0 

	def hasVisited(self, node):
		return node in self.visited

	def visit(self, node):
		self.visited.add(node)
		self.distance += graph[self.curr][node]
		self.curr = node

	def isDone(self):
		return len(graph) == len(self.visited)

graph = {}
minDistance = -1

file = open(sys.argv[1],'r')
for line in file:
	args = line.strip().split()

	node1 = args[0]
	node2 = args[2]
	dist = int(args[4])

	if node1 not in graph:
		graph[node1] = {}
	graph[node1][node2] = dist

	if node2 not in graph:
		graph[node2] = {}
	graph[node2][node1] = dist


q = Queue()
for node in graph.keys():
	q.put(Path(node))

while not q.empty():
	path = q.get()

	for nxt in graph[path.curr]:
		if not path.hasVisited(nxt):
			newPath = deepcopy(path)
			newPath.visit(nxt)

			if newPath.isDone():
				if minDistance == -1 or newPath.distance < minDistance:
					minDistance = newPath.distance
			else:
				q.put(newPath)

	del path

print(minDistance)