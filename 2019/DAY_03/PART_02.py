import sys, math

def getVisited(paths):
	visited = {};
	x = 0
	y = 0
	steps = 0

	for p in paths:
		direction = p[0]
		length = int(p[1:])

		for i in range(length):
			if (direction == 'R'):
				x += 1;
			elif (direction == 'U'):
				y += 1;
			elif (direction == 'D'):
				y -= 1;
			else:
				x -= 1;

			steps += 1
			point = "%i,%i" % (x, y)

			if (point not in visited):
				visited[point] = steps;

	return visited


file = open(sys.argv[1], 'r')

wire1 = file.readline().strip().split(",");
wire2 = file.readline().strip().split(",");

visited1 = getVisited(wire1)
visited2 = getVisited(wire2)

intersection = visited1.keys() & visited2.keys()
minSteps = sys.maxsize

for key in intersection:
	steps = visited1[key] + visited2[key]
	if steps < minSteps:
		minSteps = steps;

print(minSteps)

file.close()