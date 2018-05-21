import re

MAX_ROWS = 6
MAX_COLS = 50

def getLights(path):

	grid = []
	for row in range(MAX_ROWS):
		grid.append([])
		for col in range(MAX_COLS):
			grid[row].append(' ')

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

			for i in range(offset):
				last = grid[row].pop()
				grid[row].insert(0, last)

		elif line.startswith("rotate column"):
			instr = line[16:].split(' by ')
			col = int(instr[0])
			offset = int(instr[1])

			columnCopy = []

			for y in range(MAX_ROWS):
				columnCopy.append(grid[y][col])

			for y in range(MAX_ROWS):
				grid[(y + offset) % MAX_ROWS][col] = columnCopy[y]

	file.close()

	f = open('output.txt','w')

	for row in range(MAX_ROWS):
		for col in range(MAX_COLS):
			f.write(grid[row][col])
		f.write('\n')

	f.close()

getLights("input.txt")
