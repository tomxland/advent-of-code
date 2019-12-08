import sys, math, itertools

def getNums():
	file = open(sys.argv[1], 'r')

	line = file.readline().strip().split(",");
	nums = [[],[],[],[],[]]
	pos = [0,0,0,0,0]

	for val in line:
		for i in range(5):
			nums[i].append(int(val))

	file.close()
	return nums

def run(inputs, ampNum, nums, pos):
	opcode = 0
	i = pos[ampNum]

	while opcode != 99 or i >= len(nums[ampNum]):
		modes = [0,0,0]
		instr = nums[ampNum][i]

		opcode = instr % 100;
		instr //= 100;

		for j in range(3):
			modes[j] = instr % 10;
			instr //= 10;

		if opcode == 99:
			break

		elif opcode == 3:
			index = nums[ampNum][i+1]
			nums[ampNum][index] = inputs[-1]
			inputs.pop()
			i += 2;

		elif opcode == 4:
			index = nums[ampNum][i+1]
			pos[ampNum] = i + 2
			return nums[ampNum][index]

		else:
			a = nums[ampNum][nums[ampNum][i+1]] if modes[0] == 0 else nums[ampNum][i+1]
			b = nums[ampNum][nums[ampNum][i+2]] if modes[1] == 0 else nums[ampNum][i+2]

			if opcode == 1:
				index = nums[ampNum][i+3]
				nums[ampNum][index] = a + b
				i += 4;

			elif opcode == 2:
				index = nums[ampNum][i+3]
				nums[ampNum][index] = a * b
				i += 4;

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
				index = nums[ampNum][i+3]
				nums[ampNum][index] = 1 if a < b else 0
				i += 4

			elif opcode == 8: #equals
				index = nums[ampNum][i+3]
				nums[ampNum][index] = 1 if a == b else 0
				i += 4

			else:
				print("Invalid opp code")
				break

	return False

perm = list(itertools.permutations([5,6,7,8,9]))
maxVal = 0
for amps in perm:
	nums = getNums()
	pos = [0,0,0,0,0]

	val = 0
	i = 0

	while True:
		inputs = [val]

		#Only add in for start
		if pos[i] == 0:
			inputs.append(amps[i])

		output = run(inputs, i, nums, pos)
		i = (i + 1) % 5

		if not output:
			break
		else:
			val = output

	if (val > maxVal):
		maxVal = val

print(maxVal)
