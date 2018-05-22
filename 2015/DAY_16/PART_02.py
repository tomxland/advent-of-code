import re

mfcsam = {}
file = open("ticker.txt",'r')

for line in file:
	args = re.split(r'[:,]?\s', line.strip())
	mfcsam[args[0]] = int(args[1])

file = open("input.txt",'r')

def isGiver(args):

	for i in range(2, len(args), 2):
		compound = args[i]
		amount = int(args[i+1])

		if compound == "cats" or compound == "trees":
			if mfcsam[compound] >= amount:
				return False

		elif compound == "pomeranians" or compound == "goldfish":
			if mfcsam[compound] <= amount:
				return False

		elif mfcsam[compound] != amount:
			return False 

	return True

for line in file:
	args = re.split(r'[:,]?\s', line.strip())

	if isGiver(args):
		print("Sue", args[1])
		break

file.close()