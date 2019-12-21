import sys, math, copy
from queue import PriorityQueue

grid = []

file = open(sys.argv[1], 'r')
for y, line in enumerate(file):
	row = []
	for x, ch in enumerate(line.strip()):
		row.append(ch)
	grid.append(row)
file.close()

numChanged = 1

while numChanged > 0:
    numChanged = 0
    count = 0

    for y in range (1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            ends = 0
            
            if grid[y][x].isupper():
                grid[y][x] = '.'

            if grid[y][x] == '.':
                count += 1

                if grid[y-1][x] == '#':
                    ends += 1
                if grid[y+1][x] == '#':
                    ends += 1
                if grid[y][x-1] == '#':
                    ends += 1
                if grid[y][x+1] == '#':
                    ends += 1
                
                if ends >= 3:
                    grid[y][x] = '#'
                    numChanged += 1

f = open('output.txt','w')

for row in grid:
    for ch in row:
        f.write(ch)
    f.write('\n')

f.close()

print("There are %i valid spaces in the maze. Manually count additional for backtracking" % (count + 26))