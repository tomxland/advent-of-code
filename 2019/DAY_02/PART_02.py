import sys, math

def run(noun, verb):
	file = open(sys.argv[1], 'r')

	line = file.readline().strip().split(",");
	file.close()

	nums = []

	for val in line:
		nums.append(int(val))

	nums[1] = noun;
	nums[2] = verb;

	i = 0;

	while nums[i] != 99:
		opcode = nums[i]
		a = nums[i+1]
		b = nums[i+2]
		index = nums[i+3]

		if (opcode == 1):
			nums[index] = nums[a] + nums[b]

		elif (opcode == 2):
			nums[index] = nums[a] * nums[b]

		else:
			print("Invalid opp code")
			return 0

		i += 4;

	if nums[0] == 19690720:
		return 100 * noun + verb;
	else:
		return 0


for a in range(100):
	for b in range(100):
		result = run(a,b)
		if (result > 0):
			print(result)
			break