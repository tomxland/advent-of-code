import re, sys
from queue import PriorityQueue
import z3

class Point:
	def __init__(self, x, y, z, range):
		self.x = int(x)
		self.y = int(y)
		self.z = int(z)
		self.range = int(range)

	def __gt__(self, other):
		return self.range > other.range

	def dist(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

bots = []

def getBots(input):
	file = open(sys.argv[1], 'r')
	for line in file:
		args = re.split('[=<,> ]+', line.strip())

		bots.append(Point(args[1],args[2],args[3],args[5]))

	file.close()


def getMostOverlap():
	maxCount = 0
	for this in bots:
		common = []

		count = 0
		for other in bots:
			dist = this.dist(other)
			#if there exists a common point in both ranges
			if dist < other.range + this.range:
				common.append(other)
				count += 1

		if count >= 907: # From print outs, I know theres a subsection thats at least 907
			print(count)
			x = z3.Int('x')
			y = z3.Int('y')
			z = z3.Int('z')

			s = z3.Optimize()

			for c in common:
				s.add(z3.If(c.x >= x, c.x - x, x - c.x) + z3.If(c.y >= y, c.y - y, y - c.y) + z3.If(c.z >= z, c.z - z, z - c.z) <= c.range)

			minDist = s.minimize(z3.If(x >= 0, x, -x) + z3.If(y >= 0, y, -y) + z3.If(z >= 0, z, -z))
			if (s.check()):
				print(s.lower(minDist), s.upper(minDist))
		

	return count;

getBots(sys.argv[1])
print(getMostOverlap())
#print(getMostInRange())