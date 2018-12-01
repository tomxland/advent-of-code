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
while count < 10000000:
  if x >= len(grid) or x < 0 or y < 0 or y >= len(grid):
    expandGrid()
    x += 1
    y += 1

  if grid[y][x] == '#':
    grid[y][x] = 'F'
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

  elif grid[y][x] == '.':
    grid[y][x] = 'W'
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

  elif grid[y][x] == 'W':
    grid[y][x] = '#'
    infections += 1
    if dir == 'U':
      y -= 1

    elif dir == 'R':
      x += 1

    elif dir == 'D':
      y += 1

    elif dir == 'L':
      x -= 1

  elif grid[y][x] == 'F':
    grid[y][x] = '.'
    if dir == 'U':
      y += 1
      dir = 'D'

    elif dir == 'R':
      x -= 1
      dir = 'L'

    elif dir == 'D':
      y -= 1
      dir = 'U'

    elif dir == 'L':
      x += 1
      dir = 'R'

  count += 1

print(infections)