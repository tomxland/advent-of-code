import sys
from copy import deepcopy

file = open(sys.argv[1], 'r')

grid = []

for line in file:
	row = []
	for ch in line.strip():
		row.append(ch)

	grid.append(row)

states = set()

while True:
	prev = deepcopy(grid)

	for y, row in enumerate(grid):
		for x, space in enumerate(row):
			count = 0

			if y > 0 and prev[y-1][x] == "#":
				count += 1

			if y < len(prev) - 1 and prev[y+1][x] == "#":
				count += 1

			if x > 0 and prev[y][x-1] == "#":
				count += 1

			if x < len(prev[0]) - 1 and prev[y][x+1] == "#":
				count += 1

			#A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
			if space == '#' and count != 1:
				grid[y][x] = '.'

			#An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
			elif space == '.' and (count == 1 or count == 2):
				grid[y][x] = '#'

	state = ""

	for row in grid:
		state += "".join(row)

	if state in states:
		break
	else:
		states.add(state)

rating = 0

for i, space in enumerate(state):
	if space == '#':
		rating += pow(2,i)

print("The biodiversity rating for the first layout that appears twice is", rating)
