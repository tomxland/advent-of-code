firewall = {}

def isSafe(offset):
	safe = True

	for depth, range in firewall.items():
		posSize = range * 2 - 2
		pos = (depth + offset) % posSize

		if pos > posSize/2:
			pos = posSize - pos

		if pos == 0:
			safe = False
			break

	return safe

def getFirstSafeDelay():
	delay = 0
	while not isSafe(delay):
		delay += 1

	print(delay)


def buildFirewall(path):
	file = open(path,'r');
	for line in file:
		line = line.replace(':','').strip()
		args = line.split()
		firewall[int(args[0])] = int(args[1])

buildFirewall("input.txt")
getFirstSafeDelay()