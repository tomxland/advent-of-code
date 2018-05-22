import re

file = open("input.txt", 'r')

def getSignal(wire):
	if wire.isdigit():
		return int(wire)
	elif isinstance(signals[wire], int):
		return signals[wire]

	gate = signals[wire].split()

	if len(gate) == 1:
		val = getSignal(gate[0])
	elif gate[0] == "NOT":
		val = ~ getSignal(gate[1]) % 65536

	else:
		a = getSignal(gate[0])
		b = getSignal(gate[2])

		if gate[1] == "AND":
			val = a & b % 65536
		elif gate[1] == "OR":
			val = a | b % 65536
		elif gate[1] == "LSHIFT":
			val = a << b % 65536
		elif gate[1] == "RSHIFT":
			val = a >> b % 65536
		else:
			val = 0

	signals[wire] = val
	return val

signals = {}

for line in file:
	instr = re.split(r' -> ',line.strip())

	val = instr[0]
	if val.isdigit():
		val = int(val)

	signals[instr[1]] = val

signals['b'] = 3176

print(getSignal("a"))