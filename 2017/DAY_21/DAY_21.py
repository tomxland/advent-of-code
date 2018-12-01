import re, sys
from queue import Queue

RULE_BOOK = {}

def rotate(pattern):
  grid = pattern.split('/')
  size = len(grid)
  r = []

  for col in range(size):
    newRow = ""
    for row in range(size):
      newRow += grid[size - 1 - row][col]
    r.append(newRow)

  return "/".join(r)

def vertFlip(pattern):
  grid = pattern.split('/')
  size = len(grid)
  f = []

  for row in range(size):
    f.append(grid[size - 1 - row])

  return "/".join(f)

def horizFlip(pattern):
  grid = pattern.split('/')
  size = len(grid)
  f = []

  for row in range(size):
    newRow = ""
    for col in range(size):
      newRow += grid[row][size - 1 - col]
    f.append(newRow)

  return "/".join(f)

file = open(sys.argv[1],'r')
for line in file:
  rule = re.split("[=>\s]+", line.strip())

  toAdd = [rule[0]]
  toAdd.append(vertFlip(rule[0]))
  toAdd.append(horizFlip(rule[0]))

  rotate90 = rotate(rule[0])
  toAdd.append(rotate90)
  toAdd.append(vertFlip(rule[0]))
  toAdd.append(horizFlip(rule[0]))

  rotate180 = rotate(rotate90)
  toAdd.append(rotate180)
  toAdd.append(vertFlip(rotate90))
  toAdd.append(horizFlip(rotate90))

  rotate270 = rotate(rotate180)
  toAdd.append(rotate270)
  toAdd.append(vertFlip(rotate270))
  toAdd.append(horizFlip(rotate270))

  for pattern in toAdd:
    if pattern not in RULE_BOOK:
      RULE_BOOK[pattern] = rule[1]

file.close()

count = 0
grid = [".#.","..#","###"]

while count < int(sys.argv[2]):
  size = len(grid)

  if size % 2 == 0:
    subSize = 2
  elif size % 3 == 0:
    subSize = 3

  newGrid = []

  for i in range(size // subSize):
    outputs = []

    for j in range(size // subSize):
      section = []
      for row in range(subSize):
        section.append(grid[i*subSize+row][j*subSize:j*subSize+subSize])

      key = "/".join(section)
      outputs.append(RULE_BOOK[key].split('/'))

    for index in range(subSize + 1):
      newRow = ""
      for secNo in range(len(outputs)):
        newRow += outputs[secNo][index]
      newGrid.append(newRow)

  grid = newGrid
  count += 1

count = 0
for row in grid:
  count += row.count('#')

print(count)