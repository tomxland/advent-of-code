import re

file = open('input.txt','r')
text = ""

str = file.readline().strip()

count = 0
i = 0
while i < len(str):
	if str[i] == '(':
		endMarker = str.index(')',i)
		args = str[i+1:endMarker].split('x')

		numChar = int(args[0])
		numTimes = int(args[1])

		decompressed = ""

		contIndex = endMarker + numChar + 1

		for j in range(numTimes):
			decompressed += str[endMarker+1:contIndex]

		str = decompressed + str[contIndex:]
		i = 0

	else:
		i += 1
		count += 1

print(count)

