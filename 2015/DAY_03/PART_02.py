file = open("input.txt",'r')

visited = set()
visited.add("0,0")

x = [0,0]
y = [0,0]

line = file.readline().strip()

for index, ch in enumerate(line):
	i = index % 2

	if ch == '>':
		x[i] += 1
	elif ch == '<':
		x[i] -= 1
	elif ch == '^':
		y[i] += 1
	elif ch == 'v':
		y[i] -= 1

	visited.add("%d,%d" % (x[i],y[i]))

print(len(visited))