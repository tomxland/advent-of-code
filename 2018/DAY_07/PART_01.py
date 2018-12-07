import re, sys
from datetime import datetime
from queue import PriorityQueue
from collections import defaultdict

unvisited = set();
blocked = set()
blockerMap = {}
blockedMap = {}

def getSteps(path):
  file = open(path,'r');

  for line in file:
    args = line.split();

    blocker = args[1]
    blockedStep = args[7]

    unvisited.add(blockedStep);
    unvisited.add(blocker);
    blocked.add(blockedStep);

    if blockedStep not in blockedMap:
      blockedMap[blockedStep] = ''

    blockedMap[blockedStep] += blocker;

    if blocker not in blockerMap:
      blockerMap[blocker] = list()

    blockerMap[blocker].append(blockedStep);

def getOrder():
  order = "";
  available = PriorityQueue()

  diff = unvisited.difference(blocked)

  for d in diff:
    available.put(d)

  while not available.empty():
    step = available.get()

    unvisited.remove(step)
    order += step;

    if step in blockerMap:
      newlyFreed = blockerMap[step];

      for freed in newlyFreed:
        blockedMap[freed] = blockedMap[freed].replace(step,"")

        if not blockedMap[freed]:
          available.put(freed)

  return order;

getSteps(sys.argv[1]);
print(getOrder())
