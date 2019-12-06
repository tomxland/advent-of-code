import sys, math

file = open(sys.argv[1], 'r')
orbits = {}

for line in file:
	objects = line.strip().split(")");
	orbits[objects[1]] = objects[0]

def getPath(obj):
	path = [];

	while obj != "COM":
		obj = orbits[obj]
		path.append(obj)

	return(path);

yourPath = getPath("YOU")
santaPath = getPath("SAN")

while True:
	if yourPath[-1] == santaPath[-1]:
		yourPath.pop()
		santaPath.pop()
	else:
		break

print(len(yourPath) + len(santaPath))

file.close()