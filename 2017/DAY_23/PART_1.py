instructions = []
regs = {}

for r in "abcdefgh":
	regs[r] = 0

regs['a'] = 0

file = open("input.txt",'r')

def getValue(val):
	if val in regs:
		return regs[val]
	else:
		return int(val)

for line in file:
	instr = line.strip().split()
	instructions.append(instr)

count = 0
i = 0
while i < len(instructions):
	instr = instructions[i]

	if instr[0] == "jnz" and getValue(instr[1]) != 0:
		i += getValue(instr[2])
		continue

	elif instr[0] == "set":
		regs[instr[1]] = getValue(instr[2])

	elif instr[0] == "sub":
		regs[instr[1]] -= getValue(instr[2])

	elif instr[0] == "mul":
		count += 1
		regs[instr[1]] *= getValue(instr[2])

	i += 1

print(count)