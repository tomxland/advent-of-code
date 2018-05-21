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
lowest = lows[0]
highest = map[lowest]

i = 1
while lows[i] <= highest + 1:
	highest = max(highest, map[lows[i]]) 
	i += 1

print(highest + 1)