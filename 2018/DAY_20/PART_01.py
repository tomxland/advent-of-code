from queue import PriorityQueue

path = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

file = open("input.txt",'r')
path = file.readline()

maxCount = 0
SIZE = 1001
MID = (SIZE // 2) + 1

grid = []

for i in range(SIZE):
	row = []
	for j in range(SIZE):
		if i % 2 == 0 or j % 2 == 0:
			row.append(False)
		else:
			row.append(True)

	grid.append(row)

print('Grid built')

def buildPaths(path, y, x):
	if len(path) == 0:
		return

	startGroup = None
	for i, p in enumerate(path):
		if p == 'W':
			grid[y][x-1] = True
			x -= 2

		elif p == 'E':
			grid[y][x+1] = True
			x += 2

		elif p == 'S':
			grid[y+1][x] = True
			y += 2

		elif p == 'N':
			grid[y-1][x] = True
			y -= 2

		elif p == '(':
			startGroup = i
			break

	if startGroup is not None:
		opening = 0
		closing = 0
		split = None
		endGroup = 0

		for i in range(startGroup, len(path)):
			step = path[i]

			if step == '|' and opening - 1 == closing and split is None:
				split = i
			elif step == '(':
				opening += 1
			elif step == ')':
				closing += 1

				if closing == opening:
					endGroup = i
					break

		ending = path[endGroup+1:]

		if split != None:
			group1 = path[startGroup+1:split]
			group2 = path[split+1:endGroup]
			buildPaths(group1 + ending, y, x)
			buildPaths(group2 + ending, y, x)
		else:
			group = path[startGroup+1:endGroup]
			buildPaths(group + ending, y, x)

buildPaths(path[1:-1], MID, MID)

print("paths built")


longestPath = 0
q = PriorityQueue()
q.put((0,MID,MID))

grid[MID][MID] = False

while not q.empty():
	point = q.get()
	length = point[0]
	y = point[1]
	x = point[2]

	if length > longestPath:
		longestPath = length

	if grid[y-1][x] and grid[y-2][x]:
		grid[y-2][x] = False
		q.put((length + 1, y-2, x))

	if grid[y+1][x] and grid[y+2][x]:
		grid[y+2][x] = False
		q.put((length + 1, y+2, x))

	if grid[y][x-1] and grid[y][x-2]:
		grid[y][x-2] = False
		q.put((length + 1, y, x-2))

	if grid[y][x+1] and grid[y][x+2]:
		grid[y][x+2] = False
		q.put((length + 1, y, x+2))


print(longestPath)