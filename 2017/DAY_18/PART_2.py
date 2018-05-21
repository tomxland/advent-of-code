from queue import Queue

instructions = []

regs = [{}, {}]

file = open("input.txt",'r')

def getValue(val, program):
	if val in regs[program]:
		return regs[program][val]
	else:
		return int(val)

for line in file:
	instr = line.strip().split()
	instructions.append(instr)

	try: 
		int(instr[1])
	except ValueError:
		regs[0][instr[1]] = 0
		regs[1][instr[1]] = 0

regs[1]['p'] = 1

i = [0,0]
queue = [Queue(),Queue()]
currProg = 0
count = 0

while True:

	otherProg = (currProg + 1) % 2

	if i[currProg] >= len(instructions):
		if i[otherProg] >= len(instructions):
			break
		else:
			tmp = currProg
			currProg = otherProg
			otherProg = tmp

	instr = instructions[i[currProg]]

	if instr[0] == "jgz" and getValue(instr[1], currProg) > 0:
		i[currProg] += getValue(instr[2], currProg)
		continue

	elif instr[0] == "rcv":
		if not queue[currProg].empty():
			regs[currProg][instr[1]] = queue[currProg].get()
		elif not queue[otherProg].empty():
			currProg = otherProg
			continue
		else:
			break

	elif instr[0] == "snd":
		queue[otherProg].put(getValue(instr[1], currProg))
		if currProg == 1:
			count += 1

	elif instr[0] == "set":
		regs[currProg][instr[1]] = getValue(instr[2], currProg)

	elif instr[0] == "add":
		regs[currProg][instr[1]] += getValue(instr[2], currProg)

	elif instr[0] == "mul":
		regs[currProg][instr[1]] *= getValue(instr[2], currProg)

	elif instr[0] == "mod":
		regs[currProg][instr[1]] %= getValue(instr[2], currProg)

	i[currProg] += 1

print(count)