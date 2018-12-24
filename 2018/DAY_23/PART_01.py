import re, sys

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

def getInRange():
	bots.sort(reverse = True)

	maxBot = bots[0]
	count = 0

	for b in bots:
		if maxBot.dist(b) <= maxBot.range:
			count += 1

	return count

getBots(sys.argv[1])
print(getInRange())
