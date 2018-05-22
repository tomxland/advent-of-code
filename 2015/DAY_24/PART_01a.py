import sys, itertools, copy

packages = []

file = open(sys.argv[1],'r')

total = 0
for line in file:
	weight = int(line.strip())
	total += weight
	packages.append(weight)

target = total // 3

def getQE(group):
	product = 1
	for weight in group:
		product *= weight

	return product

minQE = None

for i in range(len(packages)):
	for group in itertools.combinations(packages, i+1):
		if sum(group) == target:
			remaining = []
			for p in packages:
				if p not in group:
					remaining.append(p)

			qe = getQE(group)
			if minQE == None or qe < minQE:
				minQE = qe


	if minQE != None:
		break

print(minQE)