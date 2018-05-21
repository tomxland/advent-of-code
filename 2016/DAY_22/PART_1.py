class Node:
	def __init__(self, x, y, size, used):
		self.size = size
		self.used = used
		self.avail = size - used
		self.x = x
		self.y = y

	def equals(self, other):
		return self.x == other.x and self.y == other.y

nodes = []
count = 0
file = open("input.txt",'r')

for i, line in enumerate(file):
	if i < 2:
		continue

	details = line.strip().split()

	coords = details[0].split('-');
	x = int(coords[1][1:])
	y = int(coords[2][1:])

	size = int(details[1].replace("T", ""))
	used = int(details[2].replace("T", ""))

	nodes.append(Node(x, y, size, used))

for a in nodes:
	for b in nodes:
		if (not a.equals(b) and a.used > 0 and a.used <= b.avail):
			count += 1

print(count)