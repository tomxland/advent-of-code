import math, sys

def getIndex(x, y):

  if (x == 0 and y == 0):
    return 1

  maxCoordinate = max(abs(x),abs(y))

  outerSize = maxCoordinate * 2 + 1;
  innerSize = outerSize - 2 

  startIndex = innerSize * innerSize
  endIndex = outerSize * outerSize
  ringSize = endIndex - startIndex

  if y == maxCoordinate * -1:
    return endIndex + x + y

  elif x == maxCoordinate * -1 or y == maxCoordinate:
    return startIndex + (ringSize // 2) - x - y

  else:
    return startIndex + x + y

def getCoordinates(num):
  if num == 1:
    return [0,0]

  #find the grid's dimensions
  squareSize = int(math.ceil(math.sqrt(num)));

  if squareSize % 2 == 0:
    squareSize += 1;

  endIndex = squareSize * squareSize
  startIndex = (squareSize - 2) * (squareSize - 2)

  maxCoordinate = (squareSize - 1) // 2

  index = num - startIndex;
  edgeSize = squareSize - 1

  if index // edgeSize  == 3:
    return [(index % edgeSize) - maxCoordinate, -1 * maxCoordinate]

  elif index // edgeSize == 2:
    return [-1 * maxCoordinate, maxCoordinate - (index % edgeSize)]

  elif index // edgeSize  == 1:
    return [maxCoordinate - (index % edgeSize), maxCoordinate]

  else:
    return [maxCoordinate, (index % edgeSize) - maxCoordinate]

def getNextLargest(limit):
  results = [0,1,1]
  i = 3

  while limit >= results[-1]:
    coord = getCoordinates(i)

    sum = 0

    for x in range(3):
      for y in range(3):

        index = getIndex(coord[0] - 1 + x, coord[1] - 1 + y)

        if index < len(results):
          sum += results[index]

    results.append(sum)
    i += 1

  return results[-1]

num = int(sys.argv[1])
print(getNextLargest(num));