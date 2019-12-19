import sys, math

nums = []
REL_BASE = 0

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

def getDrone(x, y):
	file = open(sys.argv[1], 'r')
	line = file.readline().strip().split(",")
	file.close()

	global nums
	global REL_BASE

	nums = []
	REL_BASE = 0

	count = 0
	numBlocks = 0

	for val in line:
		nums.append(int(val))

	#Pad memory
	for i in range(1000):
		nums.append(0)

	opcode = 0
	i = 0

	inputs = []

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

			count += 1

			if count % 2 == 1:
				nums[index] = x
			else:
				nums[index] = y

			i += 2

		elif opcode == 4:
			a = getValue(i+1, modes[0])	
			return str(a)	
			# i += 2

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

grid = []
count = 0

for y in range(0,50):
	row = []
	for x in range(0,50):
		drone = getDrone(x,y)
		row.append(drone)
		if drone is None:
			break
		if drone == '1':
			count += 1

	grid.append(row)

for row in grid:
	print("".join(row))

print("There are %i drones affected" % count)