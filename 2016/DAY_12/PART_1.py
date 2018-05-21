instructions = []

registers = {
	"a" : 0,
	"b" : 0,
	"c" : 1,
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
		if instr[0] == "cpy":
			registers[instr[2]] = getValue(instr[1])

		elif instr[0] == "inc":
			registers[instr[1]] += 1

		elif instr[0] == "dec":
			registers[instr[1]] -= 1
		
		i += 1

print(registers["a"])

