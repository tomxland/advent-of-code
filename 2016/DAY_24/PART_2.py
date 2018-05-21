from queue import PriorityQueue
from copy import copy, deepcopy

target = '7'
grid = []
found = False

class State:
	def __init__(self, y, x):
		self.steps = 0
		self.x = x
		self.y = y

	def score(self):
		return abs(self.x - start.x) + abs(self.y - start.y)

	def __lt__(self,other):
		return self.steps < other.steps

	def __repr__(self):
		return "%d,%d" % (self.x, self.y)

	def copy(self):
		cpy = deepcopy(self)
		cpy.steps += 1
		return cpy

file = open("input.txt",'r')
for i, line in enumerate(file):
	grid.append([])
	for j, ch in enumerate(line.strip()):
		grid[i].append(ch)

		if ch == '0':
			start = State(i, j)
		elif ch == target:
			end = State(i, j)

q = PriorityQueue()
q.put((start.score(),start))


def enqueue(state):
	global found

	if nxt.x == end.x and nxt.y == end.y:
		print(nxt.steps)
		found = True
		return

	grid[nxt.y][nxt.x] = 'X'
	q.put((nxt.score(),nxt))


while not q.empty():
	state = q.get()[1]
	y = state.y
	x = state.x

	if grid[y-1][x] != '#' and grid[y-1][x] != 'X':
		nxt = state.copy()
		nxt.y -= 1
		enqueue(nxt)
		if found:
			break

	if grid[y+1][x] != '#' and grid[y+1][x] != 'X':
		nxt = state.copy()
		nxt.y += 1
		enqueue(nxt)
		if found:
			break


	if grid[y][x-1] != '#' and grid[y][x-1] != 'X':
		nxt = state.copy()
		nxt.x -= 1
		enqueue(nxt)
		if found:
			break


	if grid[y][x+1] != '#' and grid[y][x+1] != 'X':
		nxt = state.copy()
		nxt.x += 1
		enqueue(nxt)
		if found:
			break
