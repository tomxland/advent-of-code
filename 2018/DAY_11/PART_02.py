import re, sys

SERIAL_NUMBER = int(sys.argv[1])

GRID_SIZE = 300

grid = []
for i in range(GRID_SIZE):
    row = [];
    for j in range(GRID_SIZE):
        row.append(0)

    grid.append(row)


def getPowerLevel(x, y):
    rackId = x + 10;
    powerLevel = rackId * y;
    powerLevel += SERIAL_NUMBER;
    powerLevel *= rackId;
    powerLevel = (powerLevel // 100) % 10;
    return powerLevel - 5;

def getGrid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            grid[y][x] = getPowerLevel(x+1,y+1)

def getLargestSquare():
  maxSum = -1 * sys.maxsize - 1;
  maxPoint = (0,0,0);

  for size in range(1, GRID_SIZE):
    for y in range(GRID_SIZE - size):
        for x in range(GRID_SIZE - size):
            currSum = 0;
            for yOffset in range(size):
                for xOffset in range(size):
                    currSum += grid[y+yOffset][x+xOffset]

            if currSum > maxSum:
                maxSum = currSum
                maxPoint = (x+1, y+1, size);

    print(maxPoint)
  return maxPoint

getGrid()
print(getLargestSquare())