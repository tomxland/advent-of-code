import sys, math

sum = 0;

file = open(sys.argv[1], 'r')
for line in file:

	mass = int(line.strip())

	while (mass > 0):
		mass = math.floor(mass / 3) - 2

		if (mass > 0):
			sum += mass

print(sum)