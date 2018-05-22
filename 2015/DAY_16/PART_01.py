import re

sue = {}
file = open("ticker.txt",'r')

for line in file:
	args = re.split(r'[:,]?\s', line.strip())
	sue[args[0]] = int(args[1])

file = open("input.txt",'r')

def isGiver(args):
	for i in range(2, len(args), 2):
		compound = args[i]
		amount = int(args[i+1])

		if sue[compound] != amount:
			return False

	return True

for line in file:
	args = re.split(r'[:,]?\s', line.strip())

	if isGiver(args):
		print("Sue", args[1])
		break

file.close()