import sys

grid = []

def expandGrid():
  blankRow = []
  for i in range(len(grid) + 2):
    blankRow.append('.')

  for row in grid:
    row.insert(0,'.')
    row.append('.')

  grid.insert(0,list(blankRow)) 
  grid.append(list(blankRow))


file = open(sys.argv[1],'r')
for line in file:
  row = []
  for node in line.strip():
    row.append(node)
  grid.append(row)

file.close()
x = len(grid)//2
y = x
dir = 'U'

count = 0
infections = 0
while count < 10000:
  if x >= len(grid) or x < 0 or y < 0 or y >= len(grid):
    expandGrid()
    x += 1
    y += 1

  if grid[y][x] == '#':
    grid[y][x] = '.'
    if dir == 'U':
      x += 1
      dir = 'R'

    elif dir == 'R':
      y += 1
      dir = 'D'

    elif dir == 'D':
      x -= 1
      dir = 'L'

    elif dir == 'L':
      y -= 1
      dir = 'U'

  else:
    grid[y][x] = '#'
    infections += 1
    if dir == 'U':
      x -= 1
      dir = 'L'

    elif dir == 'R':
      y -= 1
      dir = 'U'

    elif dir == 'D':
      x += 1
      dir = 'R'

    elif dir == 'L':
      y += 1
      dir = 'D'

  count += 1

print(infections)