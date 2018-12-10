import re, sys

path = sys.argv[1]

file = open(path,'r');

xPositions = [];
yPositions = [];
velocities = [];


for line in file:
	args = re.split("[<>, ]+", line.strip());
	print(args)

	xPositions.append(int(args[1]));
	yPositions.append(int(args[2]));
	velocities.append((int(args[4]), int(args[5])))

NUM_POSITIONS = len(xPositions);

for seconds in range(int(sys.argv[2])):


	for i, vel in enumerate(velocities):
		xPositions[i] += vel[0];
		yPositions[i] += vel[1]

	maxX = max(xPositions)
	minX = min(xPositions)
	maxY = max(yPositions)
	minY = min(yPositions)

	if (maxX - minX < 200 and maxY - minY < 200):
		grid = []
		for y in range(minY, maxY + 1):
			row = []
			for x in range(minX, maxX + 1):
				row.append(' ')
			grid.append(row)

		for i in range(NUM_POSITIONS):
			x = xPositions[i] - minX;
			y = yPositions[i] - minY;
			grid[y][x] = '#'

		f = open("output/"+ str(seconds + 1) + ".txt", "w")

		for row in grid:
			f.write("\n" + "".join(row))

		f.close()

	print("After " + str(seconds) + " seconds: ")
	print("X Diff: ", maxX - minX)
	print("Y Diff: ", maxY - minY)