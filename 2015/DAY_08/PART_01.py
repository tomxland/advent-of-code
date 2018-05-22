import ast, re

literalCount = 0
memoryCount = 0

file = open("input.txt", 'r')

for line in file:
	line = line.strip()
	literalCount += len(line)
	memoryCount += len(ast.literal_eval(line))

print(literalCount - memoryCount)