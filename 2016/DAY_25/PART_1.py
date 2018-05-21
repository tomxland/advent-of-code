import re

instructions = []

def getValue(str):
	if str in registers:
		return registers[str]
	else:
		return int(str)

file = open("input.txt",'r');
for line in file:
	instructions.append(line.strip().split())

pattern = re.compile("^(01)*0?$")

a = 0
while True:
	print("Testing %d" % a)
	registers = {
		"a" : a,
		"b" : 0,
		"c" : 0,
		"d" : 0
	}

	i = 0
	output = ""
	while i < len(instructions):
		instr = instructions[i]

		if instr[0] == "jnz" and getValue(instr[1]) != 0:
			i += getValue(instr[2])
		else:
			if instr[0] == "cpy":
				registers[instr[2]] = getValue(instr[1])

			elif instr[0] == "inc":
				registers[instr[1]] += 1

			elif instr[0] == "dec":
				registers[instr[1]] -= 1

			elif instr[0] == "out":
				output += str(getValue(instr[1]))

				if not pattern.match(output):
					break
			
			i += 1

	a += 1

print(registers['a'])

