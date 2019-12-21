import sys, math

base = [1, 0, -1, 0]

file = open(sys.argv[1],'r')
baseInput = file.readline()
file.close()

input = ""

offset = int(baseInput[0:7])
print("Offset is %i" % offset)

for i in range(10000):
	input += baseInput

print("Input collected")
input = input[offset:]

for k in range(100):
	sum = 0
	output = ""
	for j in range(len(input), 0, -1):
		sum += int(input[j - 1])
		sum %= 10
		output = str(sum) + output

	print("After %i phase: %s" % (k+1, output[0:8]))
	input = output