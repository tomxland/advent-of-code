import sys, math, itertools

def run(inputs):

	file = open(sys.argv[1], 'r')

	line = file.readline().strip().split(",");
	nums = []

	for val in line:
		nums.append(int(val))

	opcode = 0
	i = 0

	while opcode != 99:
		modes = [0,0,0]
		instr = nums[i]

		opcode = instr % 100;
		instr //= 100;

		for j in range(3):
			modes[j] = instr % 10;
			instr //= 10;

		if opcode == 3:
			index = nums[i+1]
			nums[index] = inputs[-1]
			inputs.pop()
			i += 2;

		elif opcode == 4:
			index = nums[i+1]
			return nums[index]

		else:
			a = nums[nums[i+1]] if modes[0] == 0 else nums[i+1]
			b = nums[nums[i+2]] if modes[1] == 0 else nums[i+2]

			if opcode == 1:
				index = nums[i+3]
				nums[index] = a + b
				i += 4;

			elif opcode == 2:
				index = nums[i+3]
				nums[index] = a * b
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
				index = nums[i+3]
				nums[index] = 1 if a < b else 0
				i += 4

			elif opcode == 8: #equals
				index = nums[i+3]
				nums[index] = 1 if a == b else 0
				i += 4

			else:
				print("Invalid opp code")
				break

	file.close()

perm = list(itertools.permutations([0,1,2,3,4]))
maxVal = 0

for amps in perm:

	val = 0
	for a in amps:
		val = run([val, a])

	if (val > maxVal):
		maxVal = val

print(maxVal)
