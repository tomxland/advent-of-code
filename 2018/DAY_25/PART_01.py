import re, sys

class Point:
	def __init__(self, coords):
		self.t = int(coords[0])
		self.x = int(coords[1])
		self.y = int(coords[2])
		self.z = int(coords[3])

	def __repr__(self):
		return "%i,%i,%i,%i" % (self.t, self.x, self.y, self.z)

	def dist(self, other):
		return abs(self.t - other.t) + abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

constellations = {}
id = 0

file = open(sys.argv[1], 'r')
for line in file:
	coords = re.split(',', line.strip())
	curr = Point(coords)

	connections = set()

	for i, key in enumerate(constellations):
		const = constellations[key]
		for p in const:
			if curr.dist(p) <= 3:
				connections.add(key)

	newList = []
	newList.append(curr)

	if len(connections) > 0:
		for key in connections:
			newList += constellations[key]
			del constellations[key]
	
	constellations[id] = newList
	id += 1

print(len(constellations))