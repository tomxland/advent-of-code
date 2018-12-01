import sys

state = 'A'

nodes = [False]
index = 0

def moveRight(index):
  index += 1
  if index >= len(nodes):
    nodes.append(False)

  return index

def moveLeft(index):
  if index == 0:
    nodes.insert(0,False)
  else:
    index -= 1

  return index

for i in range(int(sys.argv[1])):
  if state == 'A':
    if not nodes[index]:
      nodes[index] = True
      index = moveRight(index)
      state = 'B'
    else:
      nodes[index] = False
      index = moveLeft(index)
      state = 'B'

  elif state == 'B':
    if not nodes[index]:
      nodes[index] = True
      index = moveLeft(index)
      state = 'C'
    else:
      nodes[index] = False
      index = moveRight(index)
      state = 'E'

  elif state == 'C':
    if not nodes[index]:
      nodes[index] = True
      index = moveRight(index)
      state = 'E'
    else:
      nodes[index] = False
      index = moveLeft(index)
      state = 'D'

  elif state == 'D':
    if not nodes[index]:
      nodes[index] = True
      index = moveLeft(index)
      state = 'A'
    else:
      nodes[index] = True
      index = moveLeft(index)
      state = 'A'

  elif state == 'E':
    if not nodes[index]:
      nodes[index] = False
      index = moveRight(index)
      state = 'A'
    else:
      nodes[index] = False
      index = moveRight(index)
      state = 'F'

  elif state == 'F':
    if not nodes[index]:
      nodes[index] = True
      index = moveRight(index)
      state = 'E'
    else:
      nodes[index] = True
      index = moveRight(index)
      state = 'A'

print('checksum',nodes.count(True))