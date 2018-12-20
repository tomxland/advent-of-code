from queue import PriorityQueue
from copy import deepcopy

#path = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

file = open("input.txt",'r')
path = list(file.readline())

class Point:
  def __init__(self, y, x):
    self.y = y
    self.x = x

  def __repr__(self):
    return "%i,%i" % (self.y, self.x)

maxCount = 0
SIZE = 1001
MID = (SIZE // 2) + 1

grid = []

for i in range(SIZE):
  row = []
  for j in range(SIZE):
    if i % 2 == 0 or j % 2 == 0:
      row.append(False)
    else:
      row.append(True)

  grid.append(row)

print('Grid built')

positions = [Point(MID,MID)]

stack = []

startGroup = None
for i, p in enumerate(path):
  if p == 'W':
    for pos in positions:
      grid[pos.y][pos.x-1] = True
      pos.x -= 2

  elif p == 'E':
    for pos in positions:
      grid[pos.y][pos.x+1] = True
      pos.x += 2

  elif p == 'S':
    for pos in positions:
      grid[pos.y+1][pos.x] = True
      pos.y += 2

  elif p == 'N':
    for pos in positions:
      grid[pos.y-1][pos.x] = True
      pos.y -= 2

  elif p == '(':
    stack.append({ "positions" : deepcopy(positions), "branches" : [] })

  elif p == '|':
    peak = stack[-1]
    peak['branches'] += deepcopy(positions)

    positions = deepcopy(peak['positions'])

  elif p == ')':
    peak = stack.pop()
    positions = deepcopy(peak['branches'])

print("paths built")

def printGrid():
  for i in range(SIZE):
    str = ""
    for j in range(SIZE):
      if i == MID and j == MID:
        str += "X"
      elif i % 2 == 1 and j % 2 == 1:
        str += "."
      elif grid[i][j]:
        str += " "
      else:
        str += "#"

    print(str)

longestPath = 0
count = 0

q = PriorityQueue()
q.put((0,MID,MID))

grid[MID][MID] = False

while not q.empty():
  point = q.get()
  length = point[0]
  y = point[1]
  x = point[2]

  if length >= 1000:
    count += 1

  if grid[y-1][x] and grid[y-2][x]:
    grid[y-2][x] = False
    q.put((length + 1, y-2, x))

  if grid[y+1][x] and grid[y+2][x]:
    grid[y+2][x] = False
    q.put((length + 1, y+2, x))

  if grid[y][x-1] and grid[y][x-2]:
    grid[y][x-2] = False
    q.put((length + 1, y, x-2))

  if grid[y][x+1] and grid[y][x+2]:
    grid[y][x+2] = False
    q.put((length + 1, y, x+2))


print(count)