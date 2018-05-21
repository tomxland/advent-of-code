file = open('input.txt','r')

total = 0
for line in file:
	area = 0

	dimensions = line.strip().split('x')

	l = int(dimensions[0])
	w = int(dimensions[1])
	h = int(dimensions[2])

	largest = max(l,w,h)

	length = 2*l + 2*w + 2*h - 2*largest

	total += length + l*w*h

print(total)