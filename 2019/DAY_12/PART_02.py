import sys, math

def getCycle(points):
	vels = [0,0,0,0]
	startStr = "%s,%s" % (points, vels)
	currStr = None
	count = 0

	while currStr != startStr:
		for i in range(4):
			for j in range(4):
				if points[i] < points[j]:
					vels[i] += 1
				elif points[i] > points[j]:
					vels[i] -= 1

		count += 1

		for i in range(4):
			points[i] += vels[i]

		currStr = "%s,%s" % (points, vels)

	return count

x = getCycle([-6,0,-15,-3])
y = getCycle([-5,-3,10,-8])
z = getCycle([-8,-13,-11,3])

def getLCM(a, b):
    return abs(a*b) // math.gcd(a, b)

lcm = getLCM(x,y)
lcm = getLCM(z,lcm)

print(lcm)