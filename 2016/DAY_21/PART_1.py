password = []
for ch in "cegdahbf":
	password.append(ch)

file = open("input.txt",'r')

for line in file:
	instr = line.strip().split()
	
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
				password.insert(0,password.pop())

		elif instr[1] == "left":
			for i in range(int(instr[2])):
				password.append(password.pop(0))

		else:
			index = password.index(instr[6])

			offset = 1

			if index >= 4:
				offset += 1

			for i in range(index + offset):
				password.insert(0,password.pop())


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
		pos1 = int(instr[2])
		pos2 = int(instr[5])

		password.insert(pos2, password.pop(pos1))


	print("".join(password))