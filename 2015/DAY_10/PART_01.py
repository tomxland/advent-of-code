import sys

def lookAndSay(s):
	newStr = ""
	i = 0
	count = 1

	for i in range(len(s)):
		
		if i + 1 < len(s) and s[i+1] == s[i]:
			count += 1
		else:
			newStr += "%d%s" % (count, s[i])
			count = 1

	return newStr

string = sys.argv[1]
for i in range(int(sys.argv[2])):
	string = lookAndSay(string)

print(len(string))