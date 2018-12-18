import re, sys

file = open(sys.argv[1], 'r')
MAX = 50

grid = []
original = []

for line in file:
	grid.append(line.strip())
	original.append(line.strip())

def printGrid():
	for row in grid:
		print("".join(row))


def equalsOriginal():
	for i, row in enumerate(grid):
		if grid[i] != original[i]:
			return False

	return True

def getStates(r,c):
	states = { '|' : 0, '#' : 0, '.' : 0}

	for i in range(r-1,r+2):
		for j in range(c-1, c+2):
			if i >= 0 and i < MAX and j >= 0 and j < MAX and (r != i or c != j):
				val = grid[i][j]
				states[val] += 1
	return states


printGrid()

count = 0
scores = []

while True:
	next = []

	numWood = 0
	numLumberyard = 0

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

	grid = next;
	score  = numLumberyard * numWood
	scores.append(score)

	if equalsOriginal():
		break
	else:
		count += 1

print(count)

