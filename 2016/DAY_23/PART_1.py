instructions = []

registers = {
	"a" : 12,
	"b" : 0,
	"c" : 0,
	"d" : 0
}

def getValue(str):
	if str in registers:
		return registers[str]
	else:
		return int(str)

file = open("input.txt",'r');
for line in file:
	instructions.append(line.strip().split())

i = 0
while i < len(instructions):
	instr = instructions[i]

	if instr[0] == "jnz" and getValue(instr[1]) != 0:
		i += getValue(instr[2])
	else:
		if instr[0] == "mlt":
			registers[instr[2]] *= getValue(instr[1])
			registers[instr[1]] = 0

		elif instr[0] == "cpy":
			registers[instr[2]] = getValue(instr[1])

		elif instr[0] == "inc":
			registers[instr[1]] += 1

		elif instr[0] == "dec":
			registers[instr[1]] -= 1

		elif instr[0] == "tgl":
			index = i + getValue(instr[1])

			if index >= 0 and index < len(instructions):
				if len(instructions[index]) > 2:
					if instructions[index][0] == "jnz":
						instructions[index][0] = "cpy"
					else:
						instructions[index][0] = "jnz"
				else:
					if instructions[index][0] == "inc":
						instructions[index][0] = "dec"
					else:
						instructions[index][0] = "inc"
		
		i += 1

print(registers['a'])

