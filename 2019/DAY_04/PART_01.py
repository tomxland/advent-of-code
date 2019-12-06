import sys, math

start = 172930
end = 683082

def isValid(num):
	string = str(num)

	hasDouble = False

	for i in range(1,6):
		if string[i-1] == string[i]:
			hasDouble = True
		elif string[i-1] > string[i]:
			return False

	return hasDouble


count = 0

for password in range(start, end+1):
	if isValid(password):
		count += 1

print(count)