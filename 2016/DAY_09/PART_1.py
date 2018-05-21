import re

def decompress(str):

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


			ending = str[contIndex:]
			str = str[:i] + decompressed
			i = len(str) - 1

			str += ending 

		else:
			i += 1

	return str


file = open('input.txt','r')
text = ""

for line in file:
	text += line.strip()

print(len(decompress(text)))
file.close()

