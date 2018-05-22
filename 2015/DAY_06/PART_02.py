import re

size = 1000
grid = []

for y in range(size):
	grid.append([])
	for x in range(size):
		grid[y].append(0)

file = open("input.txt", 'r')

for line in file:
	instr = re.split(r'\W',line.strip())

	if instr[0] == "toggle":
		for y in range(int(instr[1]),int(instr[4])+1):
			for x in range(int(instr[2]),int(instr[5])+1):
				grid[y][x] += 2

	else:
		offset = 1 if instr[1] == "on" else -1

		for y in range(int(instr[2]),int(instr[5])+1):
			for x in range(int(instr[3]),int(instr[6])+1):
				if grid[y][x] > 0 or offset != -1:
					grid[y][x] += offset

brightness = 0
for y in range(size):
	for x in range(size):
		brightness += grid[y][x]

print(brightness)