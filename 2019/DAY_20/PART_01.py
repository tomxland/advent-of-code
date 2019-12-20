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

		keys[key].append((i,x))

for x in range(MAZE_WIDTH):
	i = MAZE_HEIGHT - DONUT_WIDTH - 2
	key = grid[i-2][x] + grid[i-1][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x))

for x in range(MAZE_WIDTH):
	i = 1 + DONUT_WIDTH
	key = grid[i+1][x] + grid[i+2][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x))

for x in range(MAZE_WIDTH-2):
	i = MAZE_HEIGHT - 3
	key = grid[i+1][x] + grid[i+2][x]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((i,x))

for y in range(MAZE_HEIGHT):
	i = 2
	key = grid[y][i-2] + grid[y][i-1]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i))

for y in range(MAZE_HEIGHT):
	i = MAZE_WIDTH - DONUT_WIDTH - 2
	key = grid[y][i-2] + grid[y][i-1]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i))

for y in range(MAZE_HEIGHT):
	i = 1 + DONUT_WIDTH
	key = grid[y][i+1] + grid[y][i+2]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i))

for y in range(MAZE_HEIGHT - 2):
	i = MAZE_WIDTH - 3
	key = grid[y][i+1] + grid[y][i+2]

	if key.isalpha():
		if key not in keys:
			keys[key] = []

		keys[key].append((y,i))

map = {}

for k in keys.keys():
	if k != 'AA' and k != 'ZZ':
		map[keys[k][0]] = keys[k][1]
		map[keys[k][1]] = keys[k][0]

print(map)

start = keys['AA'][0]
end = keys['ZZ'][0]

q = PriorityQueue()
q.put((0, start[0], start[1]))

while not q.empty():
	obj = q.get()
	steps = obj[0]
	y = obj[1]
	x = obj[2]

	if y == end[0] and x == end[1]:
		print("Least number of steps is %i" % steps)
		break

	steps += 1

	if grid[y][x] == '.':
		grid[y][x] = 'x'
	else:
		continue

	if (y,x) in map:
		newPt = map[(y,x)]
		print("Portal from", (y,x) ," to ", newPt)
		q.put((steps, newPt[0], newPt[1]))

	q.put((steps, y-1, x))
	q.put((steps, y+1, x))
	q.put((steps, y, x-1))
	q.put((steps, y, x+1))