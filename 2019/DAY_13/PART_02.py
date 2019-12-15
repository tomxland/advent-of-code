import sys, math

class Point:
	def __init__(self,_x,_y):
		self.x = _x
		self.y = _y

file = open(sys.argv[1], 'r')
line = file.readline().strip().split(",")
file.close()

nums = []

for val in line:
	nums.append(int(val))

#Pad memory
for i in range(100):
	nums.append(0)

nums[0] = 2

grid = []
for y in range(21):
	row = []
	for x in range (35):
		row.append('?')

	grid.append(row)

count = 0
numBlocks = 0

currX = 0
currY = 0
paddleX = 0
paddleY = 0
ballX = 0

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
		if ballX < paddleX: #Move left
			nums[index] = -1

			grid[paddleY][paddleX] = ' '
			paddleX -= 1
			grid[paddleY][paddleX] = '-'
		elif ballX > paddleX: #Move right
			nums[index] = 1

			grid[paddleY][paddleX] = ' '
			paddleX += 1
			grid[paddleY][paddleX] = '-'
		else:
			nums[index] = 0

		i += 2

	elif opcode == 4:
		a = getValue(i+1, modes[0])

		if count % 3 == 0:
			currX = a
		elif count % 3 == 1:
			currY = a
		else:
			if currX == -1 and currY == 0:
				print('Score:',a)
			if a == 0: #empty
				grid[currY][currX] = ' '
			elif a == 1: #wall
				grid[currY][currX] = 'H'
			elif a == 2: #block
				grid[currY][currX] = 'X'
				numBlocks += 1
			elif a == 3: #horizonal paddle
				grid[currY][currX] = '-'
				paddleX = currX
				paddleY = currY
			elif a == 4: #ball
				if grid[currY][currX] == 'X':
					numBlocks -= 1
					if numBlocks == 0:
						opcode = 99
				grid[currY][currX] = 'o'
				ballX = currX

		count += 1
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