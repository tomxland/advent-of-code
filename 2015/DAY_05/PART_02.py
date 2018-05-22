import re

def hasDouble(string):
	return re.search(r'(\w{2})(\w)*\1',string) != None

def hasRepeat(string):
	count = 0
	for i in range(0,len(string)-2):
		if string[i] == string[i+2]:
			return True

	return False


def isNice(string):
	return hasDouble(string) and hasRepeat(string)


file = open("input.txt",'r')

count = 0
for line in file:
	if isNice(line.strip()):
		count += 1

print(count)