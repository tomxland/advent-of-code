import sys, math
from queue import PriorityQueue

INPUT = 2

grid = []

file = open(sys.argv[1], 'r')
for line in file:
	row = []
	for ch in line.strip():
		row.append(ch)
	grid.append(row)
file.close()

for row in grid:
	print("".join(row))

for y, row in enumerate(grid):
	for x, ch in enumerate(row):
		if ch == '^':
			robotY = y 
			robotX = x

print(robotY, robotX)

q = PriorityQueue()
q.put((0, [], robotY, robotX, '^'))

while not q.empty():
	obj = q.get()
	steps = obj[0] + 1
	path = obj[1]
	y = obj[2]
	x = obj[3]
	dir = obj[4]
	
	print(path)

	if dir == "^":
		if y > 0 and grid[y-1][x] == '#':
			path[-1] += 1
			q.put((steps, path, y-1, x, '^'))
		else:
			if x > 0 and grid[y][x-1] == '#':
				newPath = path.copy()
				newPath.append('L')
				newPath.append(1)
				q.put((steps, newPath, y, x-1, '<'))
				#add to queue

			if x < len(grid[0]) - 1 and grid[y][x+1] == '#':
				newPath = path.copy()
				newPath.append('R')
				newPath.append(1)
				q.put((steps, newPath, y, x+1, '>'))

	if dir == "<":
		if x > 0 and grid[y][x-1] == '#':
			path[-1] += 1
			q.put((steps, path, y, x-1, '<'))
		else:
			if y > 0 and grid[y-1][x] == '#':
				newPath = path.copy()
				newPath.append('R')
				newPath.append(1)
				q.put((steps, newPath, y-1, x, '^'))
				#add to queue

			if y < len(grid) - 1 and grid[y+1][x] == '#':
				newPath = path.copy()
				newPath.append('L')
				newPath.append(1)
				q.put((steps, newPath, y+1, x, 'v'))
	
	if dir == ">":
		if x < len(grid[0]) - 1 and grid[y][x+1] == '#':
			path[-1] += 1
			q.put((steps, path, y, x+1,'>'))
		else:
			if y < len(grid) - 1 and grid[y+1][x] == '#':
				newPath = path.copy()
				newPath.append('R')
				newPath.append(1)
				q.put((steps, newPath, y+1, x, 'v'))

			if y > 0 and grid[y-1][x] == '#':
				newPath = path.copy()
				newPath.append('L')
				newPath.append(1)
				q.put((steps, newPath, y-1, x, '^'))
				#add to queue

	if dir == "v":
		if y < len(grid) - 1 and grid[y+1][x] == '#':
			path[-1] += 1
			q.put((steps, path, y+1, x, 'v'))
		else:
			if x < len(grid[0]) - 1 and grid[y][x+1] == '#':
				newPath = path.copy()
				newPath.append('L')
				newPath.append(1)
				q.put((steps, newPath, y, x+1, '>'))
			
			if x > 0 and grid[y][x-1] == '#':
				newPath = path.copy()
				newPath.append('R')
				newPath.append(1)
				q.put((steps, newPath, y, x-1, '<'))