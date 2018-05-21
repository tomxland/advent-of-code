file = open('input.txt','r')

total = 0
for line in file:
	area = 0

	dimensions = line.strip().split('x')

	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])

	side1 = l*w
	side2 = l*h
	side3 = w*h

	total += 2*side1 + 2*side2 + 2*side3 + min(side1,side2,side3)

print(total)