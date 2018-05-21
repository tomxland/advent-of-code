lows = []
map = {}

file = open("input.txt",'r')

for line in file:
	args = line.strip().split('-')
	low = int(args[0])
	high = int(args[1])

	lows.append(low)
	map[low] = high

lows.sort()

i = 0
total = 4294967296

while i < len(lows):
	lowest = lows[i]
	highest = map[lowest]
	i += 1

	while i < len(lows) and lows[i] <= highest + 1:
		highest = max(highest, map[lows[i]]) 
		i += 1

	total -= (highest - lowest + 1)

print(total)