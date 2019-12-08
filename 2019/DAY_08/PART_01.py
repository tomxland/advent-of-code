import sys, math

img = []
row = []
layer = []
count = [0,0,0]

file = open(sys.argv[1], 'r')
line = file.readline().strip();
file.close()

MAX_WIDTH = int(sys.argv[2])
MAX_HEIGHT = int(sys.argv[3])

minZeros = sys.maxsize
minScore = 0

i = 0
j = 0
k = 0

for ch in line:
	digit = int(ch)

	if digit < 3:
		count[digit] += 1

	row.append(digit)

	i = (i + 1) % MAX_WIDTH

	if i == 0:
		layer.append(row)
		row = []

		j = (j + 1) % MAX_HEIGHT

		if j == 0:
			img.append(layer)

			if (count[0] < minZeros):
				minZeros = count[0]
				minScore = count[1] * count[2]

			count = [0,0,0]
			layer = []

			k += 1

print(minScore)