import sys, math

class Point:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;

	def dist(self):
		return abs(self.x) + abs(self.y)

	def __repr__(self):
		return "%i,%i" % (self.x, self.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(str(self))

def getVisited(paths):
	visited = set();
	x = 0;
	y = 0;

	for p in paths:
		direction = p[0]
		length = int(p[1:])

		for i in range(length):
			if (direction == 'R'):
				x += 1;
			elif (direction == 'U'):
				y += 1;
			elif (direction == 'D'):
				y -= 1;
			else:
				x -= 1;

			visited.add(Point(x,y));

	return visited


file = open(sys.argv[1], 'r')

wire1 = file.readline().strip().split(",");
wire2 = file.readline().strip().split(",");

visited1 = getVisited(wire1)
visited2 = getVisited(wire2)

intersection = visited1.intersection(visited2)

minVal = min(intersection, key=lambda x: x.dist())
print(minVal.dist())


file.close()