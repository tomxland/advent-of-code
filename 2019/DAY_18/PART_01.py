import sys, math
from queue import PriorityQueue

grid = []
startY = 0
startX = 0
numDoors = 0
numKeys = 0

file = open(sys.argv[1], 'r')
for y, line in enumerate(file):
	row = []
	for x, ch in enumerate(line.strip()):
		row.append(ch)
		if ch == '@':
			startY = y
			startX = x

		elif ch.isalpha():
			if ch.isupper():
				numDoors += 1
			else:
				numKeys += 1

	grid.append(row)
file.close()

print(numDoors, numKeys)

q = PriorityQueue()
q.put((0, startY, startX, "", ""))

states = set()

while not q.empty():
	obj = q.get()
	steps = obj[0]
	y = obj[1]
	x = obj[2]
	keys = obj[3]
	doors = obj[4]

	state = "(%i,%i) %s - %s" % (y,x,doors,keys)

	if state in states:
		continue
	else:
		states.add(state)

	#print(state)

	if len(doors) == numDoors and len(keys) == numKeys:
		print(doors, keys)
		print("Shortest path in %i steps" % steps)
		break

	steps += 1
	
	if grid[y-1][x] != '#':
		pos = grid[y-1][x]
		myKeys = keys
		myDoors = doors

		if pos.isalpha() and pos.islower() and pos not in myKeys:
			myKeys += pos
		elif pos.isalpha() and pos.isupper() and pos.lower() in myKeys and pos not in myDoors:
			myDoors += pos

		q.put((steps, y-1, x, myKeys, myDoors))
	
	if grid[y+1][x] != '#':
		pos = grid[y+1][x]
		myKeys = keys
		myDoors = doors

		if pos.isalpha() and pos.islower() and pos not in myKeys:
			myKeys += pos
		elif pos.isalpha() and pos.isupper() and pos.lower() in myKeys and pos not in myDoors:
			myDoors += pos

		q.put((steps, y+1, x, myKeys, myDoors))
	
	if grid[y][x-1] != '#':
		pos = grid[y][x-1]
		myKeys = keys
		myDoors = doors

		if pos.isalpha() and pos.islower() and pos not in myKeys:
			myKeys += pos
		elif pos.isalpha() and pos.isupper() and pos.lower() in myKeys and pos not in myDoors:
			myDoors += pos

		q.put((steps, y, x-1, myKeys, myDoors))

	if grid[y][x+1] != '#':
		pos = grid[y][x+1]
		myKeys = keys
		myDoors = doors

		if pos.isalpha() and pos.islower() and pos not in myKeys:
			myKeys += pos
		elif pos.isalpha() and pos.isupper() and pos.lower() in myKeys and pos not in myDoors:
			myDoors += pos

		q.put((steps, y, x+1, myKeys, myDoors))
