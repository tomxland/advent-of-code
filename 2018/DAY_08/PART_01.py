import re, sys

metadata = [];

def getNode(array):
  numChildren = int(array[0])
  numMetadata = int(array[1])

  offset = 2;

  while numChildren > 0:
    offset += getNode(array[offset:])
    numChildren -= 1;

  for i in range(numMetadata):
    metadata.append(int(array[i+offset]))

  return offset + numMetadata


def getTree(path):
  file = open(path,'r');
  vals = file.readline().split()
  getNode(vals)

getTree(sys.argv[1]);
print(sum(metadata));
