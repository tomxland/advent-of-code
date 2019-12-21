import sys, math, re
from queue import PriorityQueue

grid = []

file = open(sys.argv[1], 'r')
for line in file:
	row = []
	for ch in line[:-1]:
		row.append(ch)
	grid.append(row)

file.close()

DONUT_WIDTH = 25
MAZE_WIDTH = len(grid[0])
MAZE_HEIGHT = len(grid)

keys = {}

for x in range(MAZE_WIDTH):
	i = 2
	key = grid[i-2][x] + grid[i-1][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x,1))

for x in range(MAZE_WIDTH):
	i = MAZE_HEIGHT - DONUT_WIDTH - 2
	key = grid[i-2][x] + grid[i-1][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x,-1))

for x in range(MAZE_WIDTH):
	i = 1 + DONUT_WIDTH
	key = grid[i+1][x] + grid[i+2][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x,-1))

for x in range(MAZE_WIDTH-2):
	i = MAZE_HEIGHT - 3
	key = grid[i+1][x] + grid[i+2][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x,1))

for y in range(MAZE_HEIGHT):
	i = 2
	key = grid[y][i-2] + grid[y][i-1]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i,1))

for y in range(MAZE_HEIGHT):
	i = MAZE_WIDTH - DONUT_WIDTH - 2
	key = grid[y][i-2] + grid[y][i-1]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i,-1))

for y in range(MAZE_HEIGHT):
	i = 1 + DONUT_WIDTH
	key = grid[y][i+1] + grid[y][i+2]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i,-1))

for y in range(MAZE_HEIGHT - 2):
	i = MAZE_WIDTH - 3
	key = grid[y][i+1] + grid[y][i+2]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i,1))

map = {}

for k in keys.keys():
	if k != 'AA' and k != 'ZZ':
		k0 = (keys[k][0][0], keys[k][0][1])
		k1 = (keys[k][1][0], keys[k][1][1])

		map[k0] = keys[k][1]
		map[k1] = keys[k][0]

start = keys['AA'][0]
end = keys['ZZ'][0]

q = PriorityQueue()
q.put((0, start[0], start[1], 0))

visited = set()

while not q.empty():
	obj = q.get()
	steps = obj[0]
	y = obj[1]
	x = obj[2]
	level = obj[3]

	state = "%i,%i - %i" % (y, x, level)
	if grid[y][x] == '.' and state not in visited:
		visited.add(state)

		if y == end[0] and x == end[1] and level == 0:
			print("Least number of steps is %i" % steps)
			break

		steps += 1

		if (y,x) in map:
			newPt = map[(y,x)]
			newLevel = level + newPt[2]
			
			if newLevel >= 0:
				q.put((steps, newPt[0], newPt[1], newLevel))

		q.put((steps, y-1, x, level))
		q.put((steps, y+1, x, level))
		q.put((steps, y, x-1, level))
		q.put((steps, y, x+1, level))