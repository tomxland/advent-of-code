import sys, itertools

containers = []

file = open(sys.argv[1],'r')
target = int(sys.argv[2])

for line in file:
	containers.append(int(line.strip()))

count = 0
for i in range(len(containers)):
	for combination in itertools.combinations(containers, i+1):
		if sum(combination) == target:
			count += 1

print(count)