import sys
import itertools

happinessMap = {}
minDistance = -1

def getHappiness(a,b):
	if a not in happinessMap or b not in happinessMap[a]:
		return 0

	return happinessMap[a][b]

file = open(sys.argv[1],'r')
for line in file:
	args = line.strip().split()

	person1 = args[0]
	person2 = args[-1].strip('.')
	modifier = -1 if args[2] == "lose" else 1
	points = modifier * int(args[3])

	if person1 not in happinessMap:
		happinessMap[person1] = {}

	happinessMap[person1][person2] = points

happinessMap["Me"] = {}
maxScore = 0

for table in itertools.permutations(happinessMap.keys()):
	score = 0
	for i in range(len(table)):
		cur = table[i]
		prv = table[-1] if i == 0 else table[i-1]
		nxt = table[0] if i == len(table) - 1 else table[i+1]

		score += getHappiness(cur,prv) + getHappiness(cur,nxt)

	if score > maxScore:
		maxScore = score

print(maxScore)