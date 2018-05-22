import re

size = 1000
grid = []

for y in range(size):
	grid.append([])
	for x in range(size):
		grid[y].append(False)

file = open("input.txt", 'r')

for line in file:
	instr = re.split(r'\W',line.strip())

	if instr[0] == "toggle":
		for y in range(int(instr[1]),int(instr[4])+1):
			for x in range(int(instr[2]),int(instr[5])+1):
				grid[y][x] = not grid[y][x]

	else:
		flag = instr[1] == "on"
		for y in range(int(instr[2]),int(instr[5])+1):
			for x in range(int(instr[3]),int(instr[6])+1):
				grid[y][x] = flag

count = 0
for y in range(size):
	count += grid[y].count(True)

print(count)