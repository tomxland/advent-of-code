import re

def hasVowels(string):
	matches = re.findall(r'[aeiou]',string)
	return len(matches) >= 3

def hasDoubles(string):
	count = 0
	for i in range(1,len(string)):
		if string[i] == string[i-1]:
			return True

	return False

def isBlacklisted(string):
	matches = re.findall(r"ab|cd|pq|xy",string)
	return len(matches) > 0

def isNice(string):
	return hasVowels(string) and hasDoubles(string) and not isBlacklisted(string)


file = open("input.txt",'r')

count = 0
for line in file:
	if isNice(line.strip()):
		count += 1


print(count)