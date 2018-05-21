password = []
for ch in "fbgdceah":
	password.append(ch)

size = len(password)

instructions = []

file = open("input.txt",'r')

for line in file:
	instructions.append(line.strip().split())

while len(instructions) > 0:
	instr = instructions.pop()
	
	if instr[0] == "swap":
		if instr[1] == "position":
			pos1 = int(instr[2])
			pos2 = int(instr[5])
		else:
			pos1 = password.index(instr[2])
			pos2 = password.index(instr[5])

		temp = password[pos1]
		password[pos1] = password[pos2]
		password[pos2] = temp

	elif instr[0] == "rotate":
		if instr[1] == "right":
			for i in range(int(instr[2])):
				password.append(password.pop(0))

		elif instr[1] == "left":
			for i in range(int(instr[2])):
				password.insert(0,password.pop())

		else:
			newIndex = password.index(instr[6])
			for i in range(size):
				if (i != 0):
					password.append(password.pop(0))

				index = (newIndex - i) % size
				offset = 2 if index >= 4 else 1

				if newIndex == (2*index + offset) % size:
					break
			
	elif instr[0] == "reverse":
		pos1 = int(instr[2])
		pos2 = int(instr[4])

		i = 0
		while i <= (pos2-pos1) // 2:
			temp = password[pos1 + i]
			password[pos1 + i] = password[pos2 - i]
			password[pos2 - i] = temp
			i += 1

	elif instr[0] == "move":
		pos2 = int(instr[2])
		pos1 = int(instr[5])

		password.insert(pos2, password.pop(pos1))

print("".join(password))