import sys, math

inputs = "A,B,A,B,C,B,A,C,B,C\nL,12,L,8,R,10,R,10\nL,6,L,4,L,12\nR,10,L,8,L,4,R,10\nn\n"
count = 0
sum = 0
entered = False

file = open(sys.argv[1], 'r')
line = file.readline().strip().split(",")
file.close()

grid = []
row = []

nums = []

for val in line:
	nums.append(int(val))

#Pad memory
for i in range(10000):
	nums.append(0)

nums[0] = 2

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
		entered = True
		index = getIndex(i+1, modes[0])
		numVal = ord(inputs[count])
		print("inputing %i = %s" % (numVal, inputs[count]))
		nums[index] = numVal
		count += 1
		i += 2

	elif opcode == 4: #Output
		a = getValue(i+1, modes[0])

		if a > 255:
			print(a)
		else:
			print(chr(a), end='')
		
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
