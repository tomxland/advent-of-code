import ast, re

literalCount = 0
encodedCount = 0

file = open("input.txt", 'r')

for line in file:
	line = line.strip()
	literalCount += len(line)
	encodedCount += len(re.escape(line)) + 2 #add 2 for bounding "

print(encodedCount - literalCount)