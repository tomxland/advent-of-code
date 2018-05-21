discs = [11,0,11,0,2,17,0]
discSizes = [13,5,17,3,7,19,11]

timer = 0

while True:
	sum = 0
	for i in range(len(discs)):
		discs[i] = (discs[i] + 1) % discSizes[i]
		sum += (discs[i] + i) % discSizes[i]

	if sum == 0:
		print(timer)
		break

	timer += 1