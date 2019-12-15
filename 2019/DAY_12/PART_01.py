import sys, math

points = []
points.append([-6,-5,-8])
points.append([0,-3,-13])
points.append([-15,10,-11])
points.append([-3,-8,3])

vels = []
for i in range(4):
	vels.append([0,0,0])

for count in range(1000):
	print("After %i steps:" % (count + 1))

	for i, point in enumerate(points):
		print("pos=%s, vel%s" % (point, vels[i]))

		for other in points:
			for pos in range(3):
				if point[pos] < other[pos]:
					vels[i][pos] += 1
				elif point[pos] > other[pos]:
					vels[i][pos] -= 1

	for i, point in enumerate(points):
		for pos in range(3):
			point[pos] += vels[i][pos]

	print("\n")

sum = 0
for i, point in enumerate(points):
	pot = 0
	kin = 0
	for j in range(3):
		pot += abs(point[j])
		kin += abs(vels[i][j])

	sum += (pot * kin)

print("The total energy in the system after 1000 steps is %i" % sum)