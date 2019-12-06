import sys, math

file = open(sys.argv[1], 'r')
tree = {}

for line in file:
	objects = line.strip().split(")");
	tree[objects[1]] = objects[0]

count = 0

for orbit in tree.keys():
	while orbit != "COM":
		orbit = tree[orbit]
		count += 1

print(count)

file.close()