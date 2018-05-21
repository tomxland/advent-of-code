import queue

size = 1364
maze = []

class Point:
	def __init__(self,_x,_y):
		self.x = _x
		self.y = _y
		self.g = 0

	def __repr__(self):
		return "(%d,%d)" % (self.x, self.y)

	def equals(self, point):
		return self.x == point.x and self.y == point.y

for y in range(size):
	maze.append([])

	for x in range(size):

		val = '.'
		sum = x*x + 3*x + 2*x*y + y + y*y
		sum += size
		binary = "{0:b}".format(sum)

		if binary.count('1') % 2 == 1:
			val = '#'

		maze[y].append(val)


start = Point(1,1)

q = queue.Queue()
q.put(start)

locs = set()

while not q.empty():
	#find least f, get node and call it q
	current = q.get()
	x = current.x
	y = current.y

	maze[y][x] = 'O'
	locs.add(str(current))

	if current.g >= 50:
		continue

	else:
		successors = []

		if x > 0:
			successors.append(Point(x-1,y))
		if x < size - 1:
			successors.append(Point(x+1,y))
		if y > 0:
			successors.append(Point(x,y-1))
		if y < size - 1:
			successors.append(Point(x,y+1))

		for successor in successors:
			if maze[successor.y][successor.x] == '.':
				successor.g = current.g + 1
				q.put(successor)

print(len(locs))
