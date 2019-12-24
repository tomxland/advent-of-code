import sys
from copy import deepcopy

file = open(sys.argv[1], 'r')
TIME = int(sys.argv[2])

grids = []
level = []
emptyLevel = []

for line in file:
	row = []
	emptyRow = []
	for ch in line.strip():
		row.append(ch)
		emptyRow.append('.')

	level.append(row)
	emptyLevel.append(emptyRow)

grids.append(level)

for i in range(TIME):
	# add neighboring, empty layers
	grids.insert(0, deepcopy(emptyLevel))
	grids.append(deepcopy(emptyLevel))
	prev = deepcopy(grids)

	for z, layer in enumerate(grids):
		for y, row in enumerate(layer):
			for x, space in enumerate(row):
				count = 0

				#skip middle (for now)
				if x == 2 and y == 2:
					continue

				if y > 0:
					if y == 3 and x == 2:
						if z + 1 < len(grids):
							#check inside
							for x1 in range(5):
								if prev[z + 1][4][x1] == "#":
									count += 1

					elif prev[z][y-1][x] == "#":
						count += 1
				elif z > 0 and prev[z - 1][1][2] == '#':
					count += 1


				if y < 4:
					if y == 1 and x == 2:
						if z + 1 < len(grids):
							#check inside
							for x1 in range(5):
								if prev[z + 1][0][x1] == "#":
									count += 1

					elif prev[z][y+1][x] == "#":
						count += 1
				elif z > 0 and prev[z - 1][3][2] == '#':
					count += 1

				if x > 0:
					if y == 2 and x == 3:
						if z + 1 < len(grids):
							#check inside
							for y1 in range(5):
								if prev[z + 1][y1][4] == "#":
									count += 1

					elif prev[z][y][x-1] == "#":
						count += 1
				elif z > 0 and prev[z - 1][2][1] == '#':
					count += 1

				if x < 4:
					if y == 2 and x == 1:
						if z + 1 < len(grids):
							#check inside
							for y1 in range(5):
								if prev[z + 1][y1][0] == "#":
									count += 1

					elif prev[z][y][x+1] == "#":
						count += 1
				elif z > 0 and prev[z - 1][2][3] == '#':
					count += 1


				#A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
				if space == '#' and count != 1:
					grids[z][y][x] = '.'

				#An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
				elif space == '.' and (count == 1 or count == 2):
					grids[z][y][x] = '#'

count = 0
for layers in grids:
	for rows in layers:
		for space in rows:
			if space == '#':
				count += 1

print("After %i minutes, there are %i bugs" % (TIME, count))
