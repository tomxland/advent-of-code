import sys, math

sum = 0;

file = open(sys.argv[1], 'r')
for line in file:

	mass = int(line.strip())
	module = math.floor(mass / 3) - 2
	sum += module

print(sum)