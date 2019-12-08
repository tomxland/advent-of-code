import sys, math

img = []
row = []
layer = []

file = open(sys.argv[1], 'r')
line = file.readline().strip();
file.close()

MAX_WIDTH = int(sys.argv[2])
MAX_HEIGHT = int(sys.argv[3])

i = 0
j = 0
k = 0

for digit in line:
	row.append(digit)

	i = (i + 1) % MAX_WIDTH

	if i == 0:
		layer.append(row)
		row = []

		j = (j + 1) % MAX_HEIGHT

		if j == 0:
			img.append(layer)
			layer = []

			k += 1

for j in range(MAX_HEIGHT):
	finalRow = ""

	for i in range(MAX_WIDTH):
		k = 0

		while img[k][j][i] == "2" and k < len(img):
			k += 1

		val = img[k][j][i]

		if val == "0":
			val = ' '

		finalRow += val

	print(finalRow)