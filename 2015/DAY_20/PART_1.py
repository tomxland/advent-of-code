import sys, math

target = int(sys.argv[1])

house = 1

while True:
	total = 0

	for i in range(1, int(math.sqrt(house))+1):
		if house % i == 0:
			total += (i*10)
			if house//i != i:
				total += house//i*10

	print(house,total)

	if (total >= target):
		break

	house += 1

print(house)