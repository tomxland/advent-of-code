import sys, math

target = int(sys.argv[1])

house = 1

deliveries = []
deliveries.append(0)

while True:
	total = 0
	deliveries.append(0)

	for i in range(1, int(math.sqrt(house))+1):
		if house % i == 0:
			if deliveries[i] < 50:
				total += (i*11)
				deliveries[i] += 1

			factor = house//i 
			if factor != i:
				if deliveries[factor] < 50:
					deliveries[factor] += 1
					total += house//i*11

	if (total >= target):
		break

	house += 1

print(house)