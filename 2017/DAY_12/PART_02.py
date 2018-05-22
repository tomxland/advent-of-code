import re
from queue import Queue

map = {}

file = open("input.txt",'r')
for line in file:
    line = line.replace(",","")
    args = line.strip().split()

    map[args[0]] = []

    i = 2
    while i < len(args):
        map[args[0]].append(args[i])
        i += 1

q = Queue()
groups = 0

while len(map) > 0:

    start = next(iter(map))
    q.put(start)

    while not q.empty():
        node = q.get()
        if node in map:
            for child in map[node]:
                if child in map:
                    q.put(child)

            del map[node]

    groups += 1

print(groups)