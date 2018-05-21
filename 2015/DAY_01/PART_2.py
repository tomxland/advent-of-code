file = open('input.txt','r')
line = file.readline()

floor = 0
for i, ch in enumerate(line):
	if ch == '(':
		floor += 1
	elif ch == ')':
		floor -= 1

	if floor < 0:
		print(i+1)
		break