programs = []
results = []
start = ord('a')
size = 1000000000

def swap(i,j):
	temp = programs[i]
	programs[i] = programs[j]
	programs[j] = temp

for i in range(16):
	programs.append(chr(start+i))

results.append("".join(programs))

file = open("input.txt",'r');
dance = file.readline().strip().split(',')

#going to repeat after some time... find out when it repeats itself
count = 0
while True:
	for move in dance:

		if move[0] == 's':
			shift = int(move[1:])
			for i in range(shift):
				last = programs.pop()
				programs.insert(0,last)

		elif move[0] == 'x':
			pos = move[1:].split('/')
			swap(int(pos[0]),int(pos[1]))

		elif move[0] == 'p':
			pos1 = programs.index(move[1])
			pos2 = programs.index(move[3])
			swap(pos1,pos2)

	str = "".join(programs);
	count += 1

	if str == "abcdefghijklmnop":
		break
	else:
		results.append(str)

print(results[size % count])