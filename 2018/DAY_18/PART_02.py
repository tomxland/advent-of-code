import re, sys

file = open(sys.argv[1], 'r')
MAX = 50

grid = []

for line in file:
	grid.append(line.strip())

def printGrid():
	for row in grid:
		print("".join(row))

def getStates(r,c):
	states = { '|' : 0, '#' : 0, '.' : 0}

	for i in range(r-1,r+2):
		for j in range(c-1, c+2):
			if i >= 0 and i < MAX and j >= 0 and j < MAX and (r != i or c != j):
				val = grid[i][j]
				states[val] += 1
	return states


#printGrid()

scores = [0]
prev = ['']

repeat = True
count = 0
cycleStart = 0

while repeat:
	print(count)
	numWood = 0
	numLumberyard = 0
	next = []
	for r in range(MAX):
		row = ''
		for c in range(MAX):
			states = getStates(r,c)

			if grid[r][c] == '.':
				if states['|'] >= 3:
					row += '|'
					numWood += 1
				else:
					row += '.'
			elif grid[r][c] == '|':
				if states['#'] >= 3:
					row += '#'
					numLumberyard += 1
				else:
					row += '|'
					numWood += 1
			elif grid[r][c] == '#':
				if states['|'] >= 1 and states['#'] >= 1:
					row += '#'
					numLumberyard += 1
				else:
					row += '.'

		next.append(row);

	score = numWood * numLumberyard
	grid = next;
	count += 1
	gridStr = "".join(grid);

	for i, g in enumerate(prev):
		if gridStr == g:
			cycleStart = i
			repeat = False

	prev.append(gridStr)
	scores.append(score)
	cycleEnd = count

print(cycleStart, cycleEnd);
cycleLen = cycleEnd - cycleStart
index = (1000000000 - cycleStart) % cycleLen
print(scores[cycleStart + index])