import re, sys
from queue import PriorityQueue

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
		self.erosion = (self.geologic + DEPTH) % 20183

		mod = self.erosion % 3

		if mod == 0 or self.x == TARGET_X and self.y == TARGET_Y: 
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
MAX = 1000

grid = []

print('setting up grid...')

for y in range(MAX):
	row = []

	for x in range(MAX):
		row.append(Point(x,y))
	
	grid.append(row)


print('calculating type...')

for y in range(1, MAX):
	for x in range(1, MAX):
		grid[y][x].geologic = grid[y-1][x].erosion * grid[y][x-1].erosion;
		grid[y][x].setType();

def canMove(x, y, equipped):
	if x < 0 or y < 0:
		return False

	point = grid[y][x]

	if point.type == '.': # Rocky
		return equipped == 'C' or equipped == 'T'

	elif point.type == '=': # Wet
		return equipped == 'C' or equipped == 'N'

	elif point.type == '|': # Narrow
		return equipped == 'T' or equipped == 'N'

	return False

def getDistance(x,y):
	return (abs(x-TARGET_X) + abs(y-TARGET_Y))


def findShortestTime():
	states = set();

	q = PriorityQueue()
	q.put((0,0,0,0,'T'))

	while not q.empty():
		[f,time,x,y,equipped] = q.get()

		if (x,y,equipped) not in states:
			states.add((x,y,equipped)) #Prevent duplicates

			if x == TARGET_X and y == TARGET_Y and equipped == 'T':
				return time

			point = grid[y][x]

			f = getDistance(x,y) + time + 7

			if point.type == '.': # Rocky
				if equipped == 'C':
					q.put((f, time + 7, x, y, 'T'))
				elif equipped == 'T':
					q.put((f, time + 7, x, y, 'C'))

			elif point.type == '=': # Wet
				if equipped == 'C':
					q.put((f, time + 7, x, y, 'N'))
				elif equipped == 'N':
					q.put((f, time + 7, x, y, 'C'))

			elif point.type == '|': # Narrow
				if equipped == 'T':
					q.put((f, time + 7, x, y, 'N'))
				elif equipped == 'N':
					q.put((f, time + 7, x, y, 'T'))

			if canMove(x-1, y, equipped):
				f = getDistance(x-1,y) + time + 1
				q.put((f, time + 1, x-1, y, equipped))

			if canMove(x+1, y, equipped):
				f = getDistance(x+1,y) + time + 1
				q.put((f, time + 1, x+1, y, equipped))

			if canMove(x, y-1, equipped):
				f = getDistance(x,y-1) + time + 1
				q.put((f, time + 1, x, y-1, equipped))

			if canMove(x, y+1, equipped):
				f = getDistance(x,y+1) + time + 1
				q.put((f, time + 1, x, y+1, equipped))

print('finding path...')
print(findShortestTime())

