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
q.put((0, 0, startY, startX, ""))

states = set()
factor = 10
minSteps = 10000

while not q.empty():
	obj = q.get()
	steps = obj[1]
	y = obj[2]
	x = obj[3]
	keys = obj[4]

	state = "(%i,%i) %s" % (y,x,sorted(keys))

	if state in states:
		continue
	else:
		states.add(state)

	# print(state)

	if len(keys) == numKeys:
		print(keys)
		print("Shortest path in %i steps" % steps)
		break

	steps += 1
	
	if grid[y-1][x] != '#':
		pos = grid[y-1][x]
		myKeys = keys

		if pos == '@' or pos == '.':
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y-1, x, myKeys))

		elif pos.islower():
			if pos not in myKeys: #get key if you
				myKeys += pos
			
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y-1, x, myKeys))
		
		elif pos.isupper() and pos.lower() in myKeys:
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y-1, x, myKeys))
	
	if grid[y+1][x] != '#':
		pos = grid[y+1][x]
		myKeys = keys

		if pos == '@' or pos == '.':
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y+1, x, myKeys))

		elif pos.islower():
			if pos not in myKeys: #get key if you
				myKeys += pos
			
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y+1, x, myKeys))
		
		elif pos.isupper() and pos.lower() in myKeys:
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y+1, x, myKeys))
	
	if grid[y][x-1] != '#':
		pos = grid[y][x-1]
		myKeys = keys

		if pos == '@' or pos == '.':
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x-1, myKeys))

		elif pos.islower():
			if pos not in myKeys: #get key if you
				myKeys += pos
			
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x-1, myKeys))
		
		elif pos.isupper() and pos.lower() in myKeys:
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x-1, myKeys))

	if grid[y][x+1] != '#':
		pos = grid[y][x+1]
		myKeys = keys

		if pos == '@' or pos == '.':
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x+1, myKeys))

		elif pos.islower():
			if pos not in myKeys: #get key if you
				myKeys += pos
			
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x+1, myKeys))
		
		elif pos.isupper() and pos.lower() in myKeys:
			keyDiff = numKeys - len(myKeys)
			score = keyDiff + (factor*steps)
			q.put((score, steps, y, x+1, myKeys))