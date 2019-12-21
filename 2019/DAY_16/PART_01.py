import sys, math, time

start = time.time()
base = [1, 0, -1, 0]

file = open(sys.argv[1],'r')
input = file.readline()
file.close()

for k in range(100):
	output = ""
	for j in range(len(input)):
		sum = 0
		for i in range(j, len(input)):
			digit = input[i]
			index = ((i - j) // (j + 1)) % 4
			myBase = base[index]
			val = int(digit) * myBase
			sum += val

		lastDigit = str(abs(sum))[-1]
		output += lastDigit

	print("After %i phase: %s" % (k+1, output[0:8]))
	input = output

end = time.time()
print((end - start), "s")