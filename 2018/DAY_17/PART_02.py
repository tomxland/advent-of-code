import re, sys

file = open(sys.argv[1], 'r')

instr = []
xList = []
yList = []

for line in file:
	args = re.split('[=, .]+', line.strip())
	instr.append(args)

	if args[0] == 'x':
		xList.append(int(args[1]))
		yList.append(int(args[3]))
		yList.append(int(args[4]))
	else:
		yList.append(int(args[1]))
		xList.append(int(args[3]))
		xList.append(int(args[4]))

maxX = max(xList)
minX = min(xList)
maxY = max(yList)
minY = min(yList)

grid = []
for i in range(maxY + 1):
	row = []
	for j in range(minX - 1, maxX + 2):
		row.append('.')
	grid.append(row)

WATER_SOURCE = 500 - minX + 1
grid[0][WATER_SOURCE] = '+'

#set up clay
for line in instr:
	if line[0] == 'x':
		x = int(line[1]) - minX + 1
		y1 = int(line[3])
		y2 = int(line[4])

		for y in range(y1, y2+1):
			grid[y][x] = '#'
	elif line[0] == 'y':
		y = int(line[1])
		x1 = int(line[3]) - minX + 1
		x2 = int(line[4]) - minX + 1

		for x in range(x1, x2+1):
			grid[y][x] = '#'	

def runWater(y,x):
	while(grid[y][x] != '#' and grid[y][x] != '~'):
		grid[y][x] = '|'
		y += 1

		if y > maxY:
			return

	settledRight = True
	settledLeft = True

	while settledRight and settledLeft:
		y -= 1
		myY = y
		leftX = x

		while grid[myY][leftX-1] != '#' and (grid[myY+1][leftX] == '#' or grid[myY+1][leftX] == '~'):
			leftX -= 1

		if grid[myY+1][leftX] != '#' and grid[myY+1][leftX] != '~':
			settledLeft = False

		rightX = x

		while grid[myY][rightX+1] != '#' and (grid[myY+1][rightX] == '#' or grid[myY+1][rightX] == '~'):
			rightX += 1

		if grid[myY+1][rightX] != '#' and grid[myY+1][rightX] != '~':
			settledRight = False

		for j in range(leftX, rightX+1):
			grid[y][j] = '~' if settledRight and settledLeft else '|'

		if not settledRight:
			if grid[y][rightX] == '.' or grid[y][rightX] == '|':
				runWater(y,rightX)

		if not settledLeft:
			if grid[y][leftX] == '.' or grid[y][leftX] == '|':
				runWater(y,leftX)

y = 1
x = WATER_SOURCE
runWater(y,x)

count = 0

for i in range(minY, maxY+1):
	for ch in grid[i]:
		if ch == '~':
			count += 1

print(count)
