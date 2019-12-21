import sys, math

class Point:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;

	def dist(self):
		return abs(self.x) + abs(self.y)

	def slope(self, other):
		quad = 0

		if self.y > other.y:
			if self.x > other.x:
				quad = 1
			else:
				quad = 2
		else:
			if self.x > other.x:
				quad = 3
			else:
				quad = 4

		if self.x == other.x:
			return "Inf Q%i" % quad
		else:
			slope = (self.y - other.y) / (self.x - other.x) 
			return "%f Q%i" % (slope, quad)

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
maxPoint = None;

for a in asteroids:
	visible = set()

	for b in asteroids:
		if a != b:
			slope = str(a.slope(b))
			if slope not in visible:
				visible.add(slope)

	view = len(visible)

	if view > maxView:
		maxView = view
		maxPoint = a

print("The optimal monitoring station (%s) can detect %i asteroids" % (maxPoint, maxView))