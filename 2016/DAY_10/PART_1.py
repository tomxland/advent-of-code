import re

values = {}
instructions = {}
outputs = {}

def addValue(bot, val):
	if bot not in values:
		values[bot] = [val]

	else:
		if val < values[bot][0]:
			values[bot].insert(0,val)
		else: 
			values[bot].append(val)

		performInstruction(bot)

def placeOutput(bin, val):
	if bin not in outputs:
		outputs

def performInstruction(bot):
	if bot in values and len(values[bot]) == 2 and bot in instructions:

		if (values[bot][0] == 17 and values[bot][1] == 61):
			print(bot)

		args = instructions[bot]
		if args[0] == "bot":
			addValue(int(args[1]), values[bot][0])
		else:
			outputs[int(args[1])] = values[bot][0]

		if args[2] == "bot":
			addValue(int(args[3]), values[bot][1])
		else:
			outputs[int(args[3])] = values[bot][1]

def readFile(input):
	file = open(input,'r')
	for line in file:
		args = line.strip().split()

		if args[0] == 'value':
			bot = int(args[5])
			value = int(args[1])

			addValue(bot, value)
		else:
			bot = int(args[1])
			instr = [args[5], args[6], args[10], args[11]]
			instructions[bot] = instr
			performInstruction(bot)

	file.close()

readFile('input.txt')
print(outputs[0] * outputs[1] * outputs[2])
