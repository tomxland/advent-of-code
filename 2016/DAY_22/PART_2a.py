from copy import copy, deepcopy
from queue import PriorityQueue

MAX_X = 36
MAX_Y = 26
SIZE_GRID = []
START_GRID = []
visited = set()

class State:
	def __init__(self, grid, dataX, dataY):
		self.dataX = dataX
		self.dataY = dataY
		self.steps = 0
		self.grid = deepcopy(grid)

	def __repr__(self):
		string = ""
		for y in range(MAX_Y + 1):
			string += "/" + ",".join(str(x) for x in self.grid[y])

		return string

	def __lt__(self,other):
		return (self.dataX + self.dataY) < (other.dataX + other.dataY)


	def copy(self):
		cpy = deepcopy(self)
		cpy.steps += 1
		return cpy

	def canMove(self, x, y, dir):
		x2 = x
		y2 = y

		if dir == 'U':
			y2 -= 1
		elif dir == 'D':
			y2 += 1
		elif dir == 'L':
			x2 -= 1
		elif dir == 'R':
			x2 += 1

		return self.grid[y][x] > 0 and self.grid[y][x] <= (SIZE_GRID[y2][x2] - self.grid[y2][x2])

	def move(self, x, y, dir):
		x2 = x
		y2 = y

		if dir == 'U':
			y2 -= 1
		elif dir == 'D':
			y2 += 1
		elif dir == 'L':
			x2 -= 1
		elif dir == 'R':
			x2 += 1

		self.grid[y2][x2] += self.grid[y][x]
		self.grid[y][x] = 0

		if (y == self.dataY and x == self.dataX):
			self.dataY = y2
			self.dataX = x2

def populateGrid(path):
	for y in range(MAX_Y + 1):
		SIZE_GRID.append([])
		START_GRID.append([])

		for x in range(MAX_X + 1):
			SIZE_GRID[y].append(0)
			START_GRID[y].append(0)

	file = open(path,'r')

	for i, line in enumerate(file):
		if i < 2:
			continue

		details = line.strip().split()

		coords = details[0].split('-');
		x = int(coords[1][1:])
		y = int(coords[2][1:])

		size = int(details[1].replace("T", ""))
		used = int(details[2].replace("T", ""))

		SIZE_GRID[y][x] = size
		START_GRID[y][x] = used

def moveMemory(state):
	for y in range(MAX_Y + 1):
		for x in range(MAX_X + 1):
			if y > 0 and state.canMove(x, y, 'U'):
				nextState = state.copy()
				nextState.move(x, y, 'U')
				if str(nextState) not in visited:
					visited.add(str(nextState))
					dist = nextState.dataX + nextState.dataY
					q.put((dist, nextState.steps, nextState))

			if y < MAX_Y and state.canMove(x, y, 'D'):
				nextState = state.copy()
				nextState.move(x, y, 'D')
				if str(nextState) not in visited:
					visited.add(str(nextState))
					dist = nextState.dataX + nextState.dataY
					q.put((dist, nextState.steps, nextState))

			if x > 0 and state.canMove(x, y, 'L'):
				nextState = state.copy()
				nextState.move(x, y, 'L')
				if str(nextState) not in visited:
					visited.add(str(nextState))
					dist = nextState.dataX + nextState.dataY
					q.put((dist, nextState.steps, nextState))

			if x < MAX_X and state.canMove(x, y, 'R'):
				nextState = state.copy()
				nextState.move(x, y, 'R')
				if str(nextState) not in visited:
					visited.add(str(nextState))
					dist = nextState.dataX + nextState.dataY
					q.put((dist, nextState.steps, nextState))


populateGrid("real_input.txt")
q = PriorityQueue()
start = State(START_GRID, MAX_X, 0)
q.put((0,0,start))

while not q.empty():
	state = q.get()[2]

	if state.dataX == 0 and state.dataY == 0:
		print(state.steps)
		break
	else: 
		moveMemory(state)
		del state