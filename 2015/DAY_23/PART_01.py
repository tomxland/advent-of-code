import re
instructions = []

regs = {
	"a" : 1,
	"b" : 0
}

file = open("input.txt",'r')

for line in file:
	args = re.split(",? ",line.strip())

	if args[0] == "jio" or args[0] == "jie":
		args[2] = int(args[2])
	elif args[0] == "jmp":
		args[1] = int(args[1])

	instructions.append(args)

i = 0
while i < len(instructions):
	instr = instructions[i]

	r = instr[1]

	if instr[0] == "jmp":
		i += instr[1]
		continue
	elif instr[0] == "jie" and regs[r] % 2 == 0:
		i += instr[2]
		continue
	elif instr[0] == "jio" and regs[r] == 1:
		i += instr[2]
		continue
	if instr[0] == "hlf":
		regs[r] //= 2
	elif instr[0] == "tpl":
		regs[r] *= 3
	elif instr[0] == "inc":
		regs[r] += 1

	i += 1

print(regs)