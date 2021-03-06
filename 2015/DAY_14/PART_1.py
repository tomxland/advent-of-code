import sys

class Reindeer:
	def __init__(self, name, speed, activeTime, restTime):
		self.name = name
		self.speed = int(speed)
		self.activeTime = int(activeTime)
		self.restTime = int(restTime)
		self.distance = 0
		self.state = self.activeTime

	def move(self):
		self.state -= 1
		if self.state >= 0:
			self.distance += self.speed
		elif self.state <= -1 * self.restTime:
			self.state = self.activeTime


reindeers = []

file = open(sys.argv[1],'r')
duration = int(sys.argv[2])

for line in file:
	args = line.strip().split()
	name = args[0]
	r = Reindeer(args[0], args[3], args[6], args[-2])
	reindeers.append(r)

for i in range(duration):
	for r in reindeers:
		r.move()

maxDist = 0
for r in reindeers:
	print(r.name, r.distance)
	if r.distance > maxDist:
		maxDist = r.distance

print(maxDist)