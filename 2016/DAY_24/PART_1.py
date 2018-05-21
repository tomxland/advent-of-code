from queue import PriorityQueue
from copy import copy, deepcopy

grid = []
visited = {}
found = {}
constants = {
	'1': 28,
	'2': 350,
	'3': 344,
	'4': 104,
	'5': 366,
	'6': 74,
	'7': 340
}

class State:
	def __init__(self, y, x):
		self.steps = 0
		self.visited = [True,False,False,False,False,False,False,False]
		self.x = x
		self.y = y

	def score(self):
		return 2*self.getLeft() + self.steps

	def getLeft(self):
		return self.visited.count(False)

	def __lt__(self,other):
		return self.steps < other.steps

	def __repr__(self):
		str = "%d,%d-" % (self.x, self.y)

		for v in self.visited:
			if v:
				str += "1"
			else:
				str += "0"

		return str

	def visit(self, num):
		self.visited[int(num)] = True

	def copy(self):
		cpy = deepcopy(self)
		cpy.steps += 1
		return cpy

file = open("input.txt",'r')
for i, line in enumerate(file):
	grid.append(line.strip())

	if '0' in line:
		y = i
		x = line.index('0')

start = State(y,x)
q = PriorityQueue()
q.put((start.getLeft(),start))


def enqueue(state):
	global found

	nxtVal = grid[nxt.y][nxt.x]

	if nxtVal.isdigit():
		nxt.visit(nxtVal)

	if nxt.getLeft() == 0:
		if nxtVal not in found:
			found[nxtVal] = nxt.steps + constants[nxtVal]
			print(found[nxtVal], nxtVal)
		return

	if str(nxt) not in visited:
		visited[str(nxt)] = nxt.steps
		q.put((nxt.score(),nxt))


while not q.empty():
	state = q.get()[1]
	y = state.y
	x = state.x

	if grid[y-1][x] != '#':
		nxt = state.copy()
		nxt.y -= 1
		enqueue(nxt)
		if len(found) == 8:
			break

	if grid[y+1][x] != '#':
		nxt = state.copy()
		nxt.y += 1
		enqueue(nxt)
		if len(found) == 8:
			break


	if grid[y][x-1] != '#':
		nxt = state.copy()
		nxt.x -= 1
		enqueue(nxt)
		if len(found) == 8:
			break


	if grid[y][x+1] != '#':
		nxt = state.copy()
		nxt.x += 1
		enqueue(nxt)
		if len(found) == 8:
			break
