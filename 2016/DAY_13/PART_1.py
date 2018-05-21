from queue import PriorityQueue

size = 1364
maze = []

class Point:
	def __init__(self,_x,_y):
		self.x = _x
		self.y = _y
		self.f = 0
		self.g = 0
		self.h = 0

	def __repr__(self):
		return "(%d,%d)" % (self.x, self.y)

	def equals(self, point):
		return self.x == point.x and self.y == point.y

	def dist(self, point):
		return abs(self.x-point.x) + abs(self.y-point.y)

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
end = Point(31,39)

startStr = str(start)

pointMap = {str(start) : start}
openQueue = PriorityQueue()
openQueue.put((0,startStr))

found = False

while not openQueue.empty() and not found:
	#find least f, get node and call it q
	currentStr = openQueue.get()[1]
	current = pointMap[currentStr]

	x = current.x
	y = current.y

	maze[y][x] = 'O'

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
		if successor.equals(end):
			found = True
			print("The shortest path is %d" % (current.g + 1))
			break
		elif maze[successor.y][successor.x] == '.':
			successor.g = current.g + 1
			successor.h = successor.dist(end)
			successor.f = successor.g + successor.h

			successorStr = str(successor)
			openQueue.put((successor.f,successorStr))
			pointMap[successorStr] = successor