import re

MAX_ROWS = 6
MAX_COLS = 50

def getNumLights(path):

	grid = []
	for row in range(MAX_ROWS):
		grid.append([])
		for col in range(MAX_COLS):
			grid[row].append('.')

	file = open('input.txt','r')
	for line in file:
		line = line.strip()

		if line.startswith("rect"): 
			dimensions = line[5:].split('x')

			for y in range(int(dimensions[1])):
				for x in range(int(dimensions[0])):
					grid[y][x] = '#'

		elif line.startswith("rotate row"):
			instr = line[13:].split(' by ')
			row = int(instr[0])
			offset = int(instr[1])

			print("row", instr)

			for i in range(offset):
				last = grid[row].pop()
				grid[row].insert(0, last)

		elif line.startswith("rotate column"):
			instr = line[16:].split(' by ')
			col = int(instr[0])
			offset = int(instr[1])

			print("col", instr)

			columnCopy = []

			for y in range(MAX_ROWS):
				columnCopy.append(grid[y][col])

			for y in range(MAX_ROWS):
				grid[(y + offset) % MAX_ROWS][col] = columnCopy[y]

	file.close()

	count = 0 
	for row in range(MAX_ROWS):
		for col in range(MAX_COLS):
			if grid[row][col] == '#':
				count += 1

	return count


print(getNumLights("input.txt"))
