import re, sys

map = {};

def getPots(path):
	file = open(path,'r');

	start = file.readline().strip();

	for line in file:
		args = re.split(" => ", line.strip());
		map[args[0]] = args[1];

	return start

pots = getPots(sys.argv[1])

offset = 0;

for generation in range(20):
	pots = "...." + pots + "....";
	newPots = ".."

	offset -= 4;

	for i in range(len(pots) - 4):
		state = pots[i:i+5]

		if state in map:
			newPots += map[state]
		else:
			newPots += "."

	newPots += ".."
	pots = newPots;

sum = 0
for i, pot in enumerate(pots):
	if pot == "#":
		sum += (i + offset)

print(sum)