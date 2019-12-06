import sys, math

start = 172930
end = 683082

def isValid(num):
	string = str(num)

	hasDouble = False
	consecutive = 1

	for i in range(1,6):
		if string[i-1] == string[i]:
			consecutive += 1
		else:
			if consecutive == 2:
				hasDouble = True

			consecutive = 1

			if string[i-1] > string[i]:
				return False

	if consecutive == 2:
		hasDouble = True

	return hasDouble


count = 0

for password in range(start, end+1):
	if isValid(password):
		count += 1

print(count)