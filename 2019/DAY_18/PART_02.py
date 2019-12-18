import sys, math
from queue import PriorityQueue

class Point:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;

	def dist(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)

	def slope(self, other):
		quad = 2

		if self.x >= other.x and self.y < other.y:
			quad = 3
		elif self.x > other.x and self.y >= other.y:
			quad = 4
		elif self.x <= other.x and self.y > other.y:
			quad = 1

		if self.x == other.x:
			return (-1*math.inf, quad)
		else:
			slope = (self.y - other.y) / (self.x - other.x) 
			return (slope, quad)

	def __repr__(self):
		return "%i,%i" % (self.x, self.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(str(self))


asteroids = set()

file = open(sys.argv[1], 'r')

y = 0
for line in file:
	x = 0
	for ch in line:
		if ch == '#':
			asteroids.add(Point(x,y));
		x += 1

	y += 1

file.close()

maxView = 0;
visible = [{}, {}, {}, {}]
station = Point(17,22)

for a in asteroids:
	if a != station:
		vals = station.slope(a)

		slope = vals[0]
		quad = vals[1] - 1

		if slope not in visible[quad]:
			visible[quad][slope] = PriorityQueue()

		dist = station.dist(a)
		print(a)
		visible[quad][slope].put((dist,a))

count = 0

#Loop through quadraints
while True:
	for v in visible:
		for key in sorted(v.keys()):
			if not v[key].empty():
				asteroid = v[key].get()[1]
				count += 1
				print("The %ith asteroid to be vaporized is %s" % (count, asteroid))
