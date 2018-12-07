import re, sys
from datetime import datetime

grid = []
coordinates = []

class Point:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)

  def setMarker(self, m):
    self.marker = m

def getDistance(a, b):
  return abs(a.x - b.x) + abs(a.y - b.y)

def getCoordinates(path):
  maxX = 0;
  maxY = 0;
  file = open(path,'r');

  for i, line in enumerate(file):
    #record = line.split();
    args = re.split("[, ]+", line.strip());

    point = Point(args[0], args[1]);
    point.setMarker(chr(ord('A') + i))

    coordinates.append(point);

    if point.x > maxX:
      maxX = point.x

    if point.y > maxY:
      maxY = point.y

  buildGrid(maxX + 1, maxY + 1);

def buildGrid(sizeX, sizeY):
  for i in range(sizeY):
    row = []
    for j in range(sizeX):
      row.append('.');

    grid.append(row);

getCoordinates(sys.argv[1]);

for y in range(len(grid)):
  for x in range(len(grid[y])):
    currPoint = Point(x, y);

    minDistance = sys.maxsize
    minCount = 0

    for coord in coordinates:
      dist = getDistance(currPoint,coord)

      if dist < minDistance:
        minCount = 1
        minDistance = dist
        grid[y][x] = coord.marker
      elif dist == minDistance:
        minCount += 1

    #account for ties
    if minCount > 1:
      grid[y][x] = '.'

edges = set()
areas = {}

for y in range(len(grid)):
  for x in range(len(grid[y])):
    if y == len(grid) - 1 or y == 0 or x == len(grid[y]) - 1 or x == 0:
      edges.add(grid[y][x]);

for y in range(len(grid)):
  for x in range(len(grid[y])):
    val = grid[y][x]
    if val not in edges:
      if val in areas:
        areas[val] += 1
      else:
        areas[val] = 1

print(max(areas.values()));
