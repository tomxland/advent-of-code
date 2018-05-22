import sys, re

weights = {}
tree = {}

def getRoot(path):

  parents = set()
  children = set()

  file = open(path,'r');

  for line in file:
    args = re.split(r'[\s\->,]+',line.strip())

    program = args[0]

    weights[program] = int(args[1][1:-1])
    tree[program] = []

    if (len(args) > 2): #means it has children
      parents.add(program)

      i = 2
      while i < len(args):
        child = args[i]
        tree[program].append(child)
        children.add(child)
        i += 1

  file.close()

  # find the parent that is not a child, i.e. the root
  return parents.difference(children).pop()

def getWeight(node):
  weight = weights[node]

  uniqueWeights = {}

  for child in tree[node]:
    w = getWeight(child)
    weight += w

    if (w not in uniqueWeights):
      uniqueWeights[w] = []

    uniqueWeights[w].append(child)

  if (len(tree[node]) > 0 and len(uniqueWeights) > 1):
    for key, value in uniqueWeights.items():
      if len(value) == 1:
        wrongWeight = key
        wrongNode = value[0]
      else:
        rightWeight = key

    diff = wrongWeight - rightWeight
    print(weights[wrongNode] - diff) #First one printed is the "corrected" weight

  return weight

root = getRoot(sys.argv[1])
getWeight(root)