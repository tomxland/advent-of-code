import queue, itertools
q = queue.Queue()

visited = {}
found = False

def toString(state):
	return ''.join(str(x) for x in state)

def isValid(state):

	chip = 2
	while (chip < len(state)):
		chipGen = chip - 1
		if state[chipGen] != state[chip]:
			gen = 1
			while (gen < len(state)):
				if gen != chipGen and state[gen] == state[chip]:
					return False
				gen += 2

		chip += 2

	return toString(state) not in visited

def visit(state, dist):
	global found
	if found:
		return

	if isEnd(state):
		found = True
		print("Shortest distance is ", dist)
	elif isValid(state):
		visited[toString(state)] = dist
		q.put(state)

def getPossibleMoves(state):
	dist = visited[toString(state)] + 1

	possibleStates = []

	elevator = state[0]

	movableItems = []
	for index, item in enumerate(state):
		if index == 0:
			continue
		elif item == elevator:
			movableItems.append(index)

	#move up
	if elevator != 4:
		for pos in movableItems:
			newMove = list(state)
			newMove[0] += 1
			newMove[pos] += 1
			visit(newMove, dist)

		for comb in itertools.combinations(movableItems, 2):
			newMove = list(state)
			newMove[0] += 1
			newMove[comb[0]] += 1
			newMove[comb[1]] += 1
			visit(newMove, dist)

	#move down
	if elevator != 1:
		for pos in movableItems:
			newMove = list(state)
			newMove[0] -= 1
			newMove[pos] -= 1
			visit(newMove, dist)

		for comb in itertools.combinations(movableItems, 2):
			newMove = list(state)
			newMove[0] -= 1
			newMove[comb[0]] -= 1
			newMove[comb[1]] -= 1
			visit(newMove, dist)


def isEnd(state):
	for floor in state:
		if floor != 4:
			return False
	return True

#start = [1,1,1,1,1,2,3,2,2,2,2]
start = [1,1,1,1,1,2,3,2,2,2,2,1,1,1,1]
#start = [1,2,1,3,1]
visited[toString(start)] = 0

q.put(start);
while not q.empty() and not found:
	getPossibleMoves(q.get())

