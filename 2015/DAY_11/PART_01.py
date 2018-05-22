import sys, re

maxDigit = ord('z')

def increment(s):
	end = ""
	for i in range(len(s)):
		pos = len(s)-1-i
		val = ord(s[pos])
		if (val >= maxDigit):
			end = 'a' + end
		else:
			end = chr(val+1) + end
			return s[0:pos] + end

	return 'a' + end

def isBlacklisted(s):
	return bool(re.search(r'[iol]', s))

def hasThreeStraight(s):
	for i in range(len(s) - 2):
		if ord(s[i]) + 2 == ord(s[i+1]) + 1 == ord(s[i+2]):
			return True

	return False

def hasTwoPairs(s):
	return bool(re.search(r'(\w)\1.*(\w)\2',s))

def isValid(s):
	return hasThreeStraight(s) and not isBlacklisted(s) and hasTwoPairs(s)

password = sys.argv[1]
while True:
	password = increment(password)
	if isValid(password):
		print(password)
		break