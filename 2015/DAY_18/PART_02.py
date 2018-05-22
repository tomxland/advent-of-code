import copy

grid = []

size = 100

def isCorner(row, col):
	return (row == 0 or row == size - 1) and (col == 0 or col == size - 1)

def isValid(row, col):
	return (0 <= row < size) and (0 <= col < size)

def getNeighborsOn(row, col):
	count = 0

	for i in range(row-1,row+2):
		for j in range(col-1,col+2):
			if isValid(i,j) and (i != row or j != col) and grid[i][j]:
				count += 1

	return count

file = open("input.txt",'r')

for i, line in enumerate(file):
	grid.append([])
	for j, ch in enumerate(line.strip()):
		grid[i].append(ch == '#' or isCorner(i,j))

for i in range(100):
	newGrid = copy.deepcopy(grid)

	for r in range(size):
		for c in range(size):
			numOn = getNeighborsOn(r,c)

			if grid[r][c]:
				newGrid[r][c] = numOn == 2 or numOn == 3 or isCorner(r,c)
			else:
				newGrid[r][c] = numOn == 3 or isCorner(r,c)

	grid = newGrid
	del newGrid

count = 0
for i in range(size):
	count += grid[i].count(True)

print(count)