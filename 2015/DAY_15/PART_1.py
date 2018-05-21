import re

properties = {}


file = open("input.txt",'r')
for line in file:
	args = re.split(r'[:,]*\s',line.strip())

	ingredient = args[0]

	i = 1
	while i < len(args):
		prop = args[i]
		val = int(args[i+1])

		if prop not in properties:
			properties[prop] = {}

		properties[prop][ingredient] = val
		i += 2


def score(amounts):
	product = 1

	for prop, propMap in properties.items():
		sum = 0
		for ingr, score in propMap.items():
			sum += amounts[ingr] * score

		if (sum < 0):
			return 0

		if prop == "calories":
			if sum != 500:
				return 0
		else:
			product *= sum

	return product

maxTsp = 100
maxScore = 0

for a in range(maxTsp + 1):
	for b in range(maxTsp + 1 - a):
		for c in range(maxTsp + 1 - a - b):
			amounts = {}
			amounts["Sugar"] = a
			amounts["Sprinkles"] = b
			amounts["Candy"] = c
			amounts["Chocolate"] = maxTsp - a - b - c
			currScore = score(amounts)

			if currScore > maxScore:
				maxScore = currScore

print(maxScore)