import re, sys

def getEndPoint(path):
  point = [0,0]

  file = open(path,'r');

  dirs = re.split(',',file.readline().strip())

  for d in dirs:
    if d == 'n':
      point[1] += 2
    elif d == 's':
      point[1] -= 2
    elif d == 'ne':
      point[0] += 1
      point[1] += 1
    elif d == 'nw':
      point[0] -= 1
      point[1] += 1
    elif d == 'se':
      point[0] += 1
      point[1] -= 1
    elif d == 'sw':
      point[0] -= 1
      point[1] -= 1

  return point

def getDistance(point):
  x = point[0]
  y = point[1]
  dist = 0

  #Move diagonally as long as you can
  while x != 0 and y != 0:
      xStep = 1
      yStep = 1

      if (x > 0):
          xStep = -1
      if (y > 0):
          yStep = -1

      x += xStep
      y += yStep
      dist += 1

  if x == 0: #If you're on the y axis, just step up/down
      dist += abs(y//2)
  else:
      dist += abs(x) #If you're on the x axis, zig zag your way back

  return dist

print(getDistance(getEndPoint(sys.argv[1])))