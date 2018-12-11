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

def getLargest3x3():
    maxSum = -1 * sys.maxsize - 1;
    maxPoint = (0,0);

    for y in range(GRID_SIZE - 3):
        for x in range(GRID_SIZE - 3):
            currSum = 0;
            for yOffset in range(3):
                for xOffset in range(3):
                    currSum += grid[y+yOffset][x+xOffset]

            if currSum > maxSum:
                maxSum = currSum
                maxPoint = (x+1, y+1);

    return maxPoint

getGrid()
print(getLargest3x3())