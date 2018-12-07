import re, sys
from datetime import datetime

grid = []
coordinates = []

SIZE = 500;
MIN_DIST = 10000;

class Point:
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)

  def setMarker(self, m):
    self.marker = m

def getDistance(a, b):
  return abs(a.x - b.x) + abs(a.y - b.y)

def getCoordinates(path):
  file = open(path,'r');

  for i, line in enumerate(file):
    #record = line.split();
    args = re.split("[, ]+", line.strip());

    point = Point(args[0], args[1]);
    point.setMarker(chr(ord('A') + i))

    coordinates.append(point);

getCoordinates(sys.argv[1]);

numSafe = 0;

for y in range(-1*SIZE,SIZE):
  for x in range(-1*SIZE,SIZE):
    isSafe = True
    currPoint = Point(x, y);
    totalDist = 0

    for coord in coordinates:
      totalDist += getDistance(currPoint,coord)

    if totalDist < MIN_DIST:
      numSafe += 1

print(numSafe);
