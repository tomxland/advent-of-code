import math, sys

def getPath(input) :
  if input == 1:
    return 0

  #find the grid's dimensions
  squareSize = math.ceil(math.sqrt(input));
  
  if squareSize % 2 == 0:
    squareSize += 1;

  #find the "index" of the input on the outer ring of the matrix
  index = input - ((squareSize - 2)*(squareSize - 2))

  #longest path will be at the corners
  longestPath = squareSize - 1;

  #shortest path will be for cells in the middle of the outer ring
  shortestPath = longestPath // 2;

  #the path of a cell is just a repeating pattern going shortest path -> longest path -> shortest path, etc
  #calculate how far the index is from the shortest path
  return shortestPath + abs(shortestPath - (index % longestPath))

num = int(sys.argv[1])
print(getPath(num));