import re, sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		if self.y == 0:
			self.geologic = self.x * 16807
			self.setType()

		elif self.x == 0:
			self.geologic = self.y * 48271
			self.setType()

		else:
			self.geologic = None
			self.erosion = None
			self.type = ' '

	def __repr__(self):
		return self.type

	def setType(self):
		if self.x == 0 and self.y == 0:
			self.type = 'M'
			self.risk = 0

		elif self.x == TARGET_X and self.y == TARGET_Y:
			self.type = 'T'
			self.risk = 0

		else:
			self.erosion = (self.geologic + DEPTH) % 20183

			mod = self.erosion % 3

			if mod == 0: 
				self.type = '.' # Rocky
				self.risk = 0
			elif mod == 1: 
				self.type = '=' # Wet
				self.risk = 1
			else:
				self.type = '|' # Narrow
				self.risk = 2

def printGrid():
	print()


	for row in grid:
		rowStr = ""
		for p in row:
			rowStr += p.type
		print(rowStr)

file = open(sys.argv[1], 'r')
DEPTH = int(file.readline().strip().split()[1]);
target = re.split('[ ,]+',file.readline().strip());
TARGET_X = int(target[1])
TARGET_Y = int(target[2])

grid = []

for y in range(TARGET_Y + 1):
	row = []

	for x in range(TARGET_X + 1):
		row.append(Point(x,y))
	
	grid.append(row)

for y in range(1, TARGET_Y + 1):
	for x in range(1, TARGET_X + 1):
		grid[y][x].geologic = grid[y-1][x].erosion * grid[y][x-1].erosion;
		grid[y][x].setType();

riskLevel = 0
for y in range(TARGET_Y + 1):
	for x in range(TARGET_X + 1):
		riskLevel += grid[y][x].risk

print(riskLevel)

