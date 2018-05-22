file = open("input.txt",'r')

visited = set()
visited.add("0,0")

x = 0
y = 0

line = file.readline().strip()

for ch in line:
	if ch == '>':
		x += 1
	elif ch == '<':
		x -= 1
	elif ch == '^':
		y += 1
	elif ch == 'v':
		y -= 1

	visited.add("%d,%d" % (x,y))

print(len(visited))