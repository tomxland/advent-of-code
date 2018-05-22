import sys, itertools

containers = []

file = open(sys.argv[1],'r')
target = int(sys.argv[2])

for line in file:
	containers.append(int(line.strip()))

count = {}
for i in range(len(containers)):
	for combination in itertools.combinations(containers, i+1):
		if sum(combination) == target:
			length = len(combination)
			if length not in count:
				count[length] = 1
			else:
				count[length] += 1

print(count[min(count)])