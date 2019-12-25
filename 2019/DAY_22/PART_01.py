import sys, math, copy

cards = []
NUM_CARDS = int(sys.argv[2])

for i in range(0, NUM_CARDS):
	cards.append(i)

file = open(sys.argv[1], 'r')
for line in file:
	arg = line.strip().split()

	if arg[0] == "cut":
		val = int(arg[1])
		if val > 0:
			cut = cards[0:val]
			cards = cards[val:] + cut

		if val < 0:
			cut = cards[val:]
			cards = cut + cards[:val]

	#deal into new stack
	elif arg[2] == "new":
		cards.reverse()

	elif arg[2] == "increment":
		val = int(arg[3])

		oldCards = copy.deepcopy(cards)
		pos = 0

		for i in range(0, NUM_CARDS):
			pos = (i * val) % NUM_CARDS
			cards[pos] = oldCards[i]

		del oldCards

file.close()

for i, c in enumerate(cards):
	if c == 2019:
		print("Card 2019 is in position %i" % i)
		break