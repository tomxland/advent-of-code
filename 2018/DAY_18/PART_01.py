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


printGrid()

for i in range(1000000000):
	next = []
	for r in range(MAX):
		row = ''
		for c in range(MAX):
			states = getStates(r,c)

			if grid[r][c] == '.':
				if states['|'] >= 3:
					row += '|'
				else:
					row += '.'
			elif grid[r][c] == '|':
				if states['#'] >= 3:
					row += '#'
				else:
					row += '|'
			elif grid[r][c] == '#':
				if states['|'] >= 1 and states['#'] >= 1:
					row += '#'
				else:
					row += '.'

		next.append(row);

	grid = next;
	#print()
	#printGrid()

numWood = 0
numLumberyard = 0

for row in grid:
	for ch in row:
		if ch == '|':
			numWood += 1
		elif ch == '#':
			numLumberyard += 1

print(numWood, 'wooded acres')
print(numLumberyard, 'lumberyards')
print('resource value', numWood * numLumberyard)

