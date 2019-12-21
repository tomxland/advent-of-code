import sys, math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dir = '^'

	def __repr__(self):
		return "%i,%i" % (self.x, self.y)

numOutputs = 0

file = open(sys.argv[1], 'r')
line = file.readline().strip().split(",")
file.close()

nums = []

for val in line:
	nums.append(int(val))

#Pad memory
for i in range(100000):
	nums.append(0)

MAX_SIZE = 150
grid = []
for y in range(MAX_SIZE):
	row = []
	for x in range(MAX_SIZE):	
		row.append('.')
	grid.append(row)

painted = set()
REL_BASE = 0
opcode = 0
i = 0

robot = Point(MAX_SIZE//2,MAX_SIZE//2)

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

	elif opcode == 3: #Input
		index = getIndex(i+1, modes[0])

		if grid[robot.y][robot.x] == '.':
			nums[index] = 0
		else:
			nums[index] = 1

		i += 2

	elif opcode == 4: #Output
		a = getValue(i+1, modes[0])

		if numOutputs % 2 == 0: #First output
			if a == 1:
				grid[robot.y][robot.x] = '#'
			else: 
				grid[robot.y][robot.x] = '.'

			painted.add(str(robot))
		else:
			if robot.dir == '^':
				if a == 0:
					robot.x -= 1
					robot.dir = '<'
				else:
					robot.x += 1
					robot.dir = '>'
			elif robot.dir == '<':
				if a == 0:
					robot.y += 1
					robot.dir = 'v'
				else:
					robot.y -= 1
					robot.dir = '^'
			elif robot.dir == 'v':
				if a == 0:
					robot.x += 1
					robot.dir = '>'
				else:
					robot.x -= 1
					robot.dir = '<'
			elif robot.dir == '>':
				if a == 0:
					robot.y -= 1
					robot.dir = '^'
				else:
					robot.y += 1
					robot.dir = 'v'

		numOutputs += 1
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

print(len(painted))

output = open("output.txt", "w")

for row in grid:
	output.write("".join(row) + "\n")

output.close()