file = open('input.txt','r')
line = file.readline()

floor = 0
for ch in line:
	if ch == '(':
		floor += 1
	elif ch == ')':
		floor -= 1

print(floor)