import re, sys

class Node:
  def __init__(self, offset, value):
    self.value = value;
    self.offset = offset

def getNode(array):
  numChildren = int(array[0])
  numMetadata = int(array[1])

  offset = 2;
  childValues = [];

  for i in range(numChildren):
    child = getNode(array[offset:])
    offset += child.offset
    childValues.append(child.value)

  value = 0

  if numChildren == 0:
    for i in range(numMetadata):
      value += int(array[i+offset])
  else:
    for i in range(numMetadata):
      index = int(array[i+offset]) - 1
      if (index < len(childValues)):
        value += childValues[index]
  
  return Node(offset + numMetadata, value)


def getTree(path):
  file = open(path,'r');
  vals = file.readline().split()
  root = getNode(vals)
  print(root.value)

getTree(sys.argv[1]);
