import re, sys
from queue import Queue

visited = set()
map = {}

file = open(sys.argv[1],'r')
for line in file:
  line = line.replace(",","")
  args = line.strip().split()

  map[args[0]] = []

  i = 2
  while i < len(args):
    map[args[0]].append(args[i])
    i += 1

start = '0'
q = Queue()
q.put(start)

while not q.empty():
  node = q.get()
  for child in map[node]:
    if child not in visited:
      visited.add(child)
      q.put(child)

print(len(visited))

file.close()