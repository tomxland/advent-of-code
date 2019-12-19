import sys, math, copy
from queue import PriorityQueue

grid = []
robots = []
numDoors = 0
numKeys = 0

file = open(sys.argv[1], 'r')
for y, line in enumerate(file):
	row = []
	for x, ch in enumerate(line.strip()):
		row.append(ch)
		if ch == '@':
			robots.append([y,x])

		elif ch.isalpha():
			if ch.isupper():
				numDoors += 1
			else:
				numKeys += 1

	grid.append(row)
file.close()

q = PriorityQueue()
q.put((0, 0, robots, ""))

states = set()
factor = 10
minSteps = 10000

count = 0

while not q.empty():
	obj = q.get()
	steps = obj[1]
	robots = copy.deepcopy(obj[2])
	keys = obj[3]

	state = "%s - %s" % (str(robots),"".join(sorted(keys)))

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

	for i, rob in enumerate(robots):
		y = rob[0]
		x = rob[1]
	
		if grid[y-1][x] != '#':
			pos = grid[y-1][x]
			myKeys = keys
			myRobots = copy.deepcopy(robots)
			myRobots[i][0] = y-1

			if pos == '@' or pos == '.':
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)

				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))

			elif pos.islower():
				if pos not in myKeys: #get key if you
					myKeys += pos
				
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)

				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
			
			elif pos.isupper() and pos.lower() in myKeys:
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
		
		if grid[y+1][x] != '#':
			pos = grid[y+1][x]
			myKeys = keys
			myRobots = copy.deepcopy(robots)
			myRobots[i][0] = y+1

			if pos == '@' or pos == '.':
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))

			elif pos.islower():
				if pos not in myKeys: #get key if you
					myKeys += pos
				
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
			
			elif pos.isupper() and pos.lower() in myKeys:
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
		
		if grid[y][x-1] != '#':
			pos = grid[y][x-1]
			myKeys = keys
			myRobots = copy.deepcopy(robots)
			myRobots[i][1] = x-1

			if pos == '@' or pos == '.':
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))

			elif pos.islower():
				if pos not in myKeys: #get key if you
					myKeys += pos
				
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
			
			elif pos.isupper() and pos.lower() in myKeys:
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))

		if grid[y][x+1] != '#':
			pos = grid[y][x+1]
			myKeys = keys
			myRobots = copy.deepcopy(robots)
			myRobots[i][1] = x+1

			if pos == '@' or pos == '.':
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)
				
				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))

			elif pos.islower():
				if pos not in myKeys: #get key if you
					myKeys += pos
				
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)

				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))
			
			elif pos.isupper() and pos.lower() in myKeys:
				keyDiff = numKeys - len(myKeys)
				score = keyDiff + (factor*steps)

				state = "%s - %s" % (str(myRobots),"".join(sorted(myKeys)))
				if state not in states:
					q.put((score, steps, myRobots, myKeys))