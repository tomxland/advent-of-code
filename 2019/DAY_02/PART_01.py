import sys, math

file = open(sys.argv[1], 'r')

line = file.readline().strip().split(",");
nums = []

for val in line:
	nums.append(int(val))

nums[1] = 12;
nums[2] = 2;

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
		break

	i += 4;

print(nums[0])

file.close()