import re, sys

xPositions = [];
yPositions = [];
velocities = [];

def getCoordinates(path):
	file = open(path,'r');

	for line in file:
		args = re.split("[<>, ]+", line.strip());

		xPositions.append(int(args[1]));
		yPositions.append(int(args[2]));
		velocities.append((int(args[4]), int(args[5])))


def getConvergence():
	seconds = 1

	while True:
		for i, vel in enumerate(velocities):
			xPositions[i] += vel[0];
			yPositions[i] += vel[1]

		maxX = max(xPositions)
		minX = min(xPositions)
		maxY = max(yPositions)
		minY = min(yPositions)

		if (maxY - minY <= 10):
			grid = []
			for y in range(minY, maxY + 1):
				row = []
				for x in range(minX, maxX + 1):
					row.append(' ')
				grid.append(row)

			for i in range(len(xPositions)):
				x = xPositions[i] - minX;
				y = yPositions[i] - minY;
				grid[y][x] = '#'

			f = open("output.txt", "w")

			for row in grid:
				f.write("".join(row) + "\n")

			f.close()
			return seconds

		else:
			seconds += 1


getCoordinates(sys.argv[1])
print(getConvergence())