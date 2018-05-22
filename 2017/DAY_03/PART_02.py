import math, sys

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
  results = [0,1]
  dictionary = {"0,0" : 1}

  i = 1

  while limit >= results[-1]:
    coord = getCoordinates(i)
    sum = 0

    for x in range(3):
      for y in range(3):
        key = "%d,%d" % (coord[0] - 1 + x, coord[1] - 1 + y)

        if key in dictionary:
          sum += results[dictionary[key]]

    dictionary["%d,%d" % (coord[0],coord[1])] = sum
    results.append(sum)
    i += 1

  return results[-1]

num = int(sys.argv[1])
print(getNextLargest(num));