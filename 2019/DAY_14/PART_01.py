import sys, re, math
from queue import Queue

class Chemical:
	def __init__(self, name, number, inputs):
		self.name = name
		self.amount = amount
		self.inputs = inputs

file = open(sys.argv[1], 'r')

formula = {}

for line in file:
	args = re.split(r'[,\W]?\s', line.strip())

	inputs = {}
	val = 0

	for i, key in enumerate(args):
		if key == '=':
			break
		elif i % 2 == 0:
			val = int(key)
		else:
			inputs[key] = val


	name = args[-1]
	amount = int(args[-2])

	chem = Chemical(name, amount, inputs)
	formula[name] = chem

file.close()

available = {}

numOre = 0
q = Queue()
q.put((1, 'FUEL'))

while not q.empty():
	vals = q.get()
	myAmount = vals[0]
	myName = vals[1]

	factor = 1
	chem = formula[myName]
	
	if myName in available and available[myName] >= 0:
		myAmount -= available[myName]
		del available[myName]

		if myAmount == 0:
			continue
		elif myAmount < 0:
			available[myName] = abs(myAmount)
			continue

	if chem.amount < myAmount:
		factor = math.ceil(myAmount / chem.amount)

	leftover = (chem.amount * factor) - myAmount

	if leftover > 0:
		if myName not in available:
			available[myName] = leftover
		else:
			available[myName] += leftover

	for key in chem.inputs.keys():
		val = chem.inputs[key] * factor
		
		if key == 'ORE':
			numOre += val
		else:
			q.put((val,key))

print("%i ORE required" % numOre)