from copy import copy, deepcopy
from queue import PriorityQueue

MAX_X = 36
MAX_Y = 26
grid = []
visited = set()

class State:
	def __init__(self, dataY, dataX, zeroY, zeroX):
		self.dataX = dataX
		self.dataY = dataY
		self.zeroX = zeroX
		self.zeroY = zeroY
		self.steps = 0

	def __repr__(self):
		return "(%d,%d)(%d,%d)" % (self.dataX, self.dataY, self.zeroX, self.zeroY)

	def __lt__(self,other):
		return (self.dataX + self.dataY) < (other.dataX + other.dataY)

	def copy(self):
		cpy = deepcopy(self)
		cpy.steps += 1
		return cpy

	def score(self):
		return self.dataX + self.dataY + self.zeroX + self.zeroY


for y in range(MAX_Y + 1):
	grid.append([])

	for x in range(MAX_X + 1):
		grid[y].append('.')

file = open("real_input.txt",'r')

for i, line in enumerate(file):
	if i < 2:
		continue

	details = line.strip().split()

	coords = details[0].split('-');
	x = int(coords[1][1:])
	y = int(coords[2][1:])

	used = int(details[2].replace("T", ""))

	if used == 0:
		empty = [y,x]
	elif used > 100:
		grid[y][x] = 'X'


start = State(0, MAX_X, empty[0], empty[1])

q = PriorityQueue()
q.put((0,0,start))

def moveMemory(state):
	if state.zeroY > 0 and grid[state.zeroY-1][state.zeroX] != 'X':
		nextState = state.copy()
		nextState.zeroY -= 1

		if nextState.zeroY == state.dataY and nextState.zeroX == state.dataX:
			nextState.dataY = state.zeroY
			nextState.dataX = state.zeroX

		if str(nextState) not in visited:
			visited.add(str(nextState))
			q.put((nextState.score(), nextState.steps, nextState))

	if state.zeroY < MAX_Y and grid[state.zeroY+1][state.zeroX] != 'X':
		nextState = state.copy()
		nextState.zeroY += 1

		if nextState.zeroY == state.dataY and nextState.zeroX == state.dataX:
			nextState.dataY = state.zeroY
			nextState.dataX = state.zeroX

		if str(nextState) not in visited:
			visited.add(str(nextState))
			q.put((nextState.score(), nextState.steps, nextState))

	if state.zeroX > 0 and grid[state.zeroY][state.zeroX-1] != 'X':
		nextState = state.copy()
		nextState.zeroX -= 1

		if nextState.zeroY == state.dataY and nextState.zeroX == state.dataX:
			nextState.dataY = state.zeroY
			nextState.dataX = state.zeroX

		if str(nextState) not in visited:
			visited.add(str(nextState))
			q.put((nextState.score(), nextState.steps, nextState))

	if state.zeroX < MAX_X and grid[state.zeroY][state.zeroX+1] != 'X':
		nextState = state.copy()
		nextState.zeroX += 1

		if nextState.zeroY == state.dataY and nextState.zeroX == state.dataX:
			nextState.dataY = state.zeroY
			nextState.dataX = state.zeroX

		if str(nextState) not in visited:
			visited.add(str(nextState))
			q.put((nextState.score(), nextState.steps, nextState))

while not q.empty():
	state = q.get()[2]

	if state.dataX == 0 and state.dataY == 0:
		print(state.steps)
		break
	else: 
		moveMemory(state)
		del state