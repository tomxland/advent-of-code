maxRows = 400000

input = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."
maxCols = len(input)
grid = [[]]

for ch in input:
	grid[0].append(ch == '.')

def isSafe(r,c):
	left = grid[r-1][c-1] if c > 0 else True
	center = grid[r-1][c]
	right = grid[r-1][c+1] if c < maxCols - 1 else True

	return not ((not left and not center and right) or 
		(left and not center and not right) or
		(not left and center and right) or
		(left and center and not right))

row = 1
while row < maxRows:
	grid.append([])
	for col in range(maxCols):
		grid[row].append(isSafe(row,col))
	row += 1

count = 0
for row in range(maxRows):
	for col in range(maxCols):
		if grid[row][col]:
			count += 1

print(count)