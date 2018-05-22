import sys, re

def parseInput(path):
  file = open(path,'r');
  array = re.split(r',+', file.readline().rstrip())
  file.close();
  return list(map(int, array));

array = []
maxSize = 256

for i in range(maxSize):
  array.append(i)

lengths = parseInput(sys.argv[1])

skipSize = 0
currPos = 0

for length in lengths:
  i = 0
  while i < length / 2:
    pos1 = (currPos + i) % maxSize
    pos2 = (currPos + length - 1 - i) % maxSize

    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp
    i += 1

  currPos = (currPos + length + skipSize) % maxSize
  skipSize += 1

print(array[0] * array[1])