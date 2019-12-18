import sys, math


MAX_SIZE = 43
grid = []
for i in range(MAX_SIZE):
	row = []
	for j in range(MAX_SIZE):
		row.append(' ')
	grid.append(row)

x = MAX_SIZE//2
y = MAX_SIZE//2
nextX = 50
nextY = 50

dir = 0

path = []

file = open(sys.argv[1], 'r')
line = file.readline().strip().split(",")
file.close()

nums = []

count = 0
numBlocks = 0

for val in line:
	nums.append(int(val))

#Pad memory
for i in range(10000):
	nums.append(0)

REL_BASE = 0
opcode = 0
i = 0

def getValue(i, mode):
	global REL_BASE
	global nums

	if mode == 0:
		return nums[nums[i]]
	elif mode == 1:
		return nums[i]
	else:
		pos = REL_BASE + nums[i]
		return nums[pos]

def getIndex(i,mode):
	global nums

	if mode == 2:
		return REL_BASE + nums[i]
	else:
		return nums[i]

while opcode != 99:
	modes = [0,0,0]
	instr = nums[i]

	opcode = instr % 100
	instr //= 100

	for j in range(3):
		modes[j] = instr % 10
		instr //= 10

	if opcode == 99:
		break

	elif opcode == 3:
		index = getIndex(i+1, modes[0])

		#if you can go:
		if grid[y-1][x] == ' ':
			nextY = y-1
			nextX = x 
			dir = 1
			path.append(dir)
		elif grid[y+1][x] == ' ':
			nextY = y+1
			nextX = x 
			dir = 2
			path.append(dir)
		elif grid[y][x-1] == ' ':
			nextY = y
			nextX = x-1
			dir = 3
			path.append(dir)
		elif grid[y][x+1] == ' ':
			nextY = y
			nextX = x+1
			dir = 4
			path.append(dir)
		else: #go back how you came
			if len(path) == 0:
				break

			prevDir = path.pop()
			if prevDir == 1:
				nextY = y+1
				nextX = x 
				dir = 2
			elif prevDir == 2:
				nextY = y-1
				nextX = x 
				dir = 1
			elif prevDir == 3:
				nextY = y
				nextX = x+1
				dir = 4
			elif prevDir == 4:
				nextY = y
				nextX = x-1
				dir = 3

		nums[index] = dir
		i += 2

	elif opcode == 4:
		a = getValue(i+1, modes[0])

		if a == 0:
			grid[nextY][nextX] = '#'
			path.pop()
		else:
			if a == 2:
				print("Shortest path is %i" % len(path))
				break

			grid[y][x] = '.'
			x = nextX
			y = nextY

		i += 2

	elif opcode == 9:
		a = getValue(i+1, modes[0])
		REL_BASE += a
		i += 2

	else:
		a = getValue(i+1, modes[0])
		b = getValue(i+2, modes[1])

		if opcode == 1:
			index = getIndex(i+3, modes[2])
			nums[index] = a + b
			i += 4

		elif opcode == 2:
			index = getIndex(i+3, modes[2])
			nums[index] = a * b
			i += 4

		elif opcode == 5: #jump-if-true
			if a != 0:
				i = b
			else:
				i += 3

		elif opcode == 6: #jump-if-false
			if a == 0:
				i = b
			else:
				i += 3

		elif opcode == 7: #less-than
			index = getIndex(i+3, modes[2])
			nums[index] = 1 if a < b else 0
			i += 4

		elif opcode == 8: #equals
			index = getIndex(i+3, modes[2])
			nums[index] = 1 if a == b else 0
			i += 4

		else:
			print("Invalid opp code")
			break